import requests
import json
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'VOTRE_TOKEN_GITHUB'
REPO_NAME = 'VotreNomUtilisateur/NomRepo'
FILE_PATH = 'SQLMap.md'  # Chemin vers la cheatsheet SQLMap sur GitHub

def fetch_sqlmap_cheatsheet():
    """Récupère la cheatsheet SQLMap depuis GitHub."""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json()['content']
        return content
    else:
        print("Erreur lors de la récupération de la cheatsheet SQLMap.")
        return None

def parse_cheatsheet_and_generate_playbook(content, target_ips):
    """Analyse la cheatsheet SQLMap et génère un playbook Ansible."""
    commands = []  # Ici, extrayez et adaptez les commandes SQLMap de la cheatsheet
    
    # Exemple simplifié de structure de playbook Ansible
    playbook = [{
        'hosts': 'all',
        'tasks': [{
            'name': 'Execute SQLMap command',
            'command': f'sqlmap {cmd} -u {ip}'  # Adaptez cette commande
        } for cmd in commands for ip in target_ips]
    }]
    
    with open('sqlmap_playbook.yml', 'w') as file:
        yaml.dump(playbook, file, allow_unicode=True)

def execute_ansible_playbook():
    """Exécute le playbook Ansible généré."""
    subprocess.run(['ansible-playbook', 'sqlmap_playbook.yml'], check=True)

def main():
    content = fetch_sqlmap_cheatsheet()
    if content:
        # Supposons que target_ips soit une liste d'IPs à cibler, récupérée précédemment
        target_ips = ['192.168.1.1']  # Exemple d'IP, remplacez par les IPs cibles réelles
        parse_cheatsheet_and_generate_playbook(content, target_ips)
        execute_ansible_playbook()

if __name__ == '__main__':
    main()
