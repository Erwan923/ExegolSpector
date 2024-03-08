import subprocess
import os
import json

# Nom de la cible Active Directory (AD) - à définir par l'utilisateur
nom_AD = "nomdomaine.local"

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande {command}: {e}")
        return None

def collecte_bloodhound():
    print("Lancement de la collecte BloodHound avec SharpHound...")
    # Exemple de commande SharpHound
    execute_command("SharpHound -c All -d " + nom_AD + " -json")

def analyse_bloodhound():
    print("Analyse des données collectées par BloodHound...")
    # Emplacement par défaut des fichiers JSON collectés par SharpHound
    fichiers_json = [f for f in os.listdir('.') if f.endswith('.json')]
    for fichier in fichiers_json:
        with open(fichier, 'r') as f:
            data = json.load(f)
            # Analyse simplifiée - Recherchez des opportunités d'élévation de privilège
            # Ceci est un exemple conceptuel. Une analyse réelle serait plus complexe.
            if "HighValueTargets" in data:
                print("Cibles à haute valeur trouvées. Tentative d'élévation de privilège...")
                # Ajoutez votre logique d'élévation de privilège ici

def main():
    print(f"Lancement de l'outil ADPrivilegeEscalationTool pour {nom_AD}")
    collecte_bloodhound()
    analyse_bloodhound()
    print("Opération terminée.")

if __name__ == "__main__":
    main()
