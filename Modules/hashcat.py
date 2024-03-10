import requests
import base64
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'VOTRE_TOKEN_GITHUB'
REPO_NAME = 'VotreNomUtilisateur/VotreRepo'
FILE_PATH = 'HashcatCheatsheet.md'  # Chemin de la cheatsheet Hashcat sur GitHub

def fetch_cheatsheet_from_github():
    """Récupère la cheatsheet Hashcat depuis GitHub."""
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
    """Génère un playbook Ansible basé sur la cheatsheet Hashcat."""
    # Exemple de logique pour extraire des commandes de la cheatsheet
    # Cette partie nécessite une adaptation en fonction du format de votre cheatsheet
    commands = ['hashcat -a 0 -m 0 hash.txt /path/to/wordlist.txt']  # Commande d'exemple

    tasks = [{'name': "Execute Hashcat commands",
              'ansible.builtin.shell': cmd,
              'become': 'yes'}  # Hashcat peut nécessiter des privilèges élevés pour l'accès matériel
              for cmd in commands]

    playbook = [{
        'hosts': 'localhost',  # Ajustez à votre cible
        'tasks': tasks
    }]

    playbook_path = 'hashcat_playbook.yml'
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
