import requests
import base64
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'VOTRE_TOKEN_GITHUB'
REPO_NAME = 'VotreNomUtilisateur/VotreRepo'
FILE_PATH = 'BettercapCheatsheet.md'  # Chemin de la cheatsheet Bettercap sur GitHub

def fetch_cheatsheet_from_github():
    """Récupère la cheatsheet Bettercap depuis GitHub."""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content_base64 = response.json()['content']
        cheatsheet_content = base64.b64decode(content_base64).decode('utf-8')
        return cheatsheet_content
    else:
        print(f"Failed to fetch cheatsheet from GitHub. Status Code: {response.status_code}")
        return None

def generate_ansible_playbook(cheatsheet_content):
    """Génère un playbook Ansible basé sur la cheatsheet Bettercap."""
    # Ici, insérez votre logique pour extraire les commandes spécifiques de Bettercap à partir de la cheatsheet.
    # Cet exemple suppose une commande simple pour la démonstration.
    commands = ['bettercap -eval "set http.proxy.sslstrip true; set http.proxy true; http.proxy on"']  # Exemple de commande

    tasks = [{'name': "Execute Bettercap commands",
              'ansible.builtin.command': cmd} for cmd in commands]

    playbook = [{
        'hosts': 'localhost',  # Modifiez selon votre cible
        'tasks': tasks
    }]

    playbook_path = 'bettercap_playbook.yml'
    with open(playbook_path, 'w') as file:
        yaml.dump(playbook, file, sort_keys=False, default_flow_style=False)

    return playbook_path

def execute_ansible_playbook(playbook_path):
    """Exécute le playbook Ansible généré."""
    subprocess.run(['ansible-playbook', playbook_path], check=True)

def main():
    cheatsheet_content = fetch_cheatsheet_from_github()
    if cheatsheet_content:
        playbook_path = generate_ansible_playbook(cheatsheet_content)
        execute_ansible_playbook(playbook_path)
    else:
        print("Could not generate Ansible playbook due to an error.")

if __name__ == "__main__":
    main()
