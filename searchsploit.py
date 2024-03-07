import requests
import base64
import yaml
import subprocess

# Configuration GitHub
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
REPO_NAME = 'your_github_username/repository_name'
FILE_PATH = 'SearchsploitCheatsheet.md'  # Chemin de la cheatsheet sur GitHub

def fetch_searchsploit_cheatsheet():
    """Fetch Searchsploit cheatsheet from GitHub."""
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

def parse_cheatsheet_and_prepare_searches(cheatsheet_content):
    """Parse the cheatsheet content to prepare searchsploit searches."""
    searches = []  # Extract search queries from the cheatsheet
    # This is a placeholder; actual logic depends on the cheatsheet's format
    return searches

def generate_ansible_playbook(search_queries):
    """Generate an Ansible playbook that executes searchsploit searches."""
    tasks = [{'name': f'Searching exploits for: {query}',
              'command': f'searchsploit {query}',
              'register': 'search_result'}
             for query in search_queries]
    playbook = [{'hosts': 'localhost', 'tasks': tasks}]
    with open('searchsploit_playbook.yml', 'w') as file:
        yaml.safe_dump(playbook, file, default_flow_style=False)

def execute_ansible_playbook():
    """Execute the generated Ansible playbook."""
    subprocess.run(['ansible-playbook', 'searchsploit_playbook.yml'], check=True)

def main():
    cheatsheet_content = fetch_searchsploit_cheatsheet()
    if cheatsheet_content:
        search_queries = parse_cheatsheet_and_prepare_searches(cheatsheet_content)
        generate_ansible_playbook(search_queries)
        execute_ansible_playbook()

if __name__ == '__main__':
    main()
