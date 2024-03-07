import requests
import base64
import yaml
import subprocess

GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
REPO_NAME = 'YourGithubUsername/YourRepo'
FILE_PATH = 'Nikto.md'

def fetch_cheatsheet(repo_name, file_path, github_token):
    headers = {'Authorization': f'token {github_token}'}
    url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return base64.b64decode(response.json()['content']).decode('utf-8')
    else:
        raise Exception("Failed to fetch cheatsheet")

def generate_ansible_playbook(command):
    playbook = [{
        'hosts': 'all',
        'tasks': [{
            'name': 'Execute Nikto Scan',
            'command': command
        }]
    }]
    with open('nikto_playbook.yml', 'w') as file:
        yaml.dump(playbook, file, allow_unicode=True)

def main():
    cheatsheet_content = fetch_cheatsheet(REPO_NAME, FILE_PATH, GITHUB_TOKEN)
    # Analyze the cheatsheet content to extract the command
    # This is simplified; you need to parse the cheatsheet to extract actual commands
    nikto_command = 'nikto -h TARGET_URL'
    generate_ansible_playbook(nikto_command)
    subprocess.run(['ansible-playbook', 'nikto_playbook.yml'], check=True)

if __name__ == '__main__':
    main()
