import requests
import json
import base64
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'VOTRE_TOKEN_GITHUB'
REPO_NAME = 'VotreNomUtilisateur/VotreRepo'
FILE_PATH = 'DNSenum.md'  # Chemin de la cheatsheet DNSenum sur GitHub

def fetch_cheatsheet(repo_name, file_path, github_token):
    """Récupère la cheatsheet depuis GitHub."""
    headers = {'Authorization': f'token {github_token}'}
    url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content_base64 = response.json()['content']
        content = base64.b64decode(content_base64).decode('utf-8')
        return content
    else:
        raise Exception("Failed to fetch cheatsheet from GitHub.")

def generate_ansible_playbook(cheatsheet_content, target):
    """Génère un playbook Ansible basé sur la cheatsheet."""
    commands = []  # Extrait les commandes de la cheatsheet, cela dépend de son format
    
    tasks = [
        {
            'name': f"Running DNSenum command on {target}",
            'command': f'dnsenum {target}'  # Utilisez une commande réelle extraite de la cheatsheet
        }
        for command in commands
    ]
    
    playbook = [
        {
            'hosts': 'localhost',
            'tasks': tasks
        }
    ]
    
    playbook_path = 'dnsenum_playbook.yml'
    with open(playbook_path, 'w') as file:
        yaml.safe_dump(playbook, file, default_flow_style=False)
    
    return playbook_path

def execute_ansible_playbook(playbook_path):
    """Exécute le playbook Ansible."""
    subprocess.run(['ansible-playbook', playbook_path], check=True)

def main():
    cheatsheet_content = fetch_cheatsheet(REPO_NAME, FILE_PATH, GITHUB_TOKEN)
    target = "example.com"  # La cible devrait être dynamiquement fournie par attack_orchestrator.py
    playbook_path = generate_ansible_playbook(cheatsheet_content, target)
    execute_ansible_playbook(playbook_path)

if __name__ == '__main__':
    main()
