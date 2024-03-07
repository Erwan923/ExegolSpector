import requests
import base64
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
REPO_NAME = 'your_github_username/repository_name'
FILE_PATH = 'MetasploitCheatsheet.md'

def fetch_metasploit_cheatsheet():
    """Fetch Metasploit cheatsheet from GitHub."""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content_base64 = response.json()['content']
        cheatsheet_content = base64.b64decode(content_base64).decode('utf-8')
        return cheatsheet_content
    else:
        print(f"Failed to fetch cheatsheet. Status code: {response.status_code}")
        return None

def parse_cheatsheet_and_generate_commands(cheatsheet_content):
    """Parse the cheatsheet content to extract Metasploit commands."""
    commands = []
    # Logic to parse cheatsheet and extract commands goes here
    # This is a placeholder; actual parsing logic depends on the cheatsheet's format
    return commands

def generate_ansible_playbook(msf_commands):
    """Generate an Ansible playbook that executes Metasploit commands."""
    tasks = [{'name': f'Executing Metasploit command: {cmd}',
              'command': f'msfconsole -x "{cmd}"'}
             for cmd in msf_commands]
    playbook = [{'hosts': 'localhost', 'tasks': tasks}]
    with open('metasploit_playbook.yml', 'w') as file:
        yaml.safe_dump(playbook, file, default_flow_style=False)

def execute_ansible_playbook():
    """Execute the generated Ansible playbook."""
    subprocess.run(['ansible-playbook', 'metasploit_playbook.yml'], check=True)

def main():
    cheatsheet_content = fetch_metasploit_cheatsheet()
    if cheatsheet_content:
        msf_commands = parse_cheatsheet_and_generate_commands(cheatsheet_content)
        generate_ansible_playbook(msf_commands)
        execute_ansible_playbook()

if __name__ == '__main__':
    main()
