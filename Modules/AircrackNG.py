import requests
import base64
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
REPO_NAME = 'your_github_username/repository_name'
FILE_PATH = 'AircrackNGCheatsheet.md'  # Chemin de la cheatsheet Aircrack-ng sur GitHub

def fetch_aircrackng_cheatsheet():
    """Fetch Aircrack-ng cheatsheet from GitHub."""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content_base64 = response.json()['content']
        cheatsheet_content = base64.b64decode(content_base64).decode('utf-8')
        return cheatsheet_content
    else:
        print("Failed to fetch cheatsheet. Status code:", response.status_code)
        return None

def parse_cheatsheet_and_generate_commands(cheatsheet_content):
    """Parse the cheatsheet content to extract Aircrack-ng commands."""
    commands = []
    # Here, extract and adapt Aircrack-ng commands from the cheatsheet.
    # This placeholder needs real logic based on the cheatsheet format.
    return commands

def generate_ansible_playbook(aircrackng_commands):
    """Generate an Ansible playbook executing Aircrack-ng commands."""
    tasks = [{'name': f'Executing Aircrack-ng command',
              'command': cmd} for cmd in aircrackng_commands]
    playbook = [{'hosts': 'localhost', 'tasks': tasks}]
    with open('aircrackng_playbook.yml', 'w') as file:
        yaml.safe_dump(playbook, file, default_flow_style=False)

def execute_ansible_playbook():
    """Execute the generated Ansible playbook."""
    subprocess.run(['ansible-playbook', 'aircrackng_playbook.yml'], check=True)

def main():
    cheatsheet_content = fetch_aircrackng_cheatsheet()
    if cheatsheet_content:
        aircrackng_commands = parse_cheatsheet_and_generate_commands(cheatsheet_content)
        generate_ansible_playbook(aircrackng_commands)
        execute_ansible_playbook()

if __name__ == '__main__':
    main()
