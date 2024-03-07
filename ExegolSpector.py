import argparse
import subprocess
import yaml
import os
import json
import xmltodict
import requests
import base64

# Configuration GitHub (utilisée pour récupérer la cheatsheet, si nécessaire)
GITHUB_TOKEN = ''
REPO_NAME = 'Erwan923/ExegolSpector'
FILE_PATH = 'Nmap.md'

def parse_args():
    parser = argparse.ArgumentParser(description="Automated Nmap Scanning with Ansible")
    parser.add_argument('--type', choices=['basic', 'discovery', 'advanced', 'port', 'version', 'aggressive'], help="Type of scan to perform")
    parser.add_argument('--targets', nargs='+', required=True, help="Target IP address(es)")
    return parser.parse_args()

def generate_ansible_playbook(commands, targets):
    playbook_path = 'nmap_playbook.yml'
    report_filename = "nmap_report.xml"
    tasks = [{
        'name': f"Executing Nmap command",
        'command': f"{command} {' '.join(targets)} -oX {report_filename}",
    } for command in commands]
    playbook = [{'hosts': 'localhost', 'tasks': tasks}]
    with open(playbook_path, 'w') as file:
        yaml.safe_dump(playbook, file, default_flow_style=False)
    return playbook_path, report_filename

def execute_ansible_playbook(playbook_path):
    subprocess.run(['ansible-playbook', playbook_path], check=True)

def convert_xml_to_json(xml_file_path):
    if os.path.exists(xml_file_path):
        with open(xml_file_path) as xml_file:
            xml_string = xml_file.read()
        json_data = xmltodict.parse(xml_string)
        json_file_path = xml_file_path.replace('.xml', '.json')
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"Scan report saved to {json_file_path}")
    else:
        print("Nmap did not generate an XML report.")

def get_markdown_from_github(repo_name, file_path, github_token):
    headers = {'Authorization': f'token {github_token}'}
    api_url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        file_content_base64 = response.json()['content']
        markdown_content = base64.b64decode(file_content_base64).decode('utf-8')
        return markdown_content
    else:
        print(f"Failed to fetch file from GitHub. Status Code: {response.status_code}")
        return None

def parse_markdown_for_commands(markdown_content, scan_type):
    scan_sections = {
        'basic': '### Basic Scanning Techniques',
        'discovery': '### Discovery Options',
        'advanced': '### Advanced Scanning Options',
        'port': '### Port Scanning Options',
        'version': '### Version Detection',
        'aggressive': '### Firewall Evasion Techniques'
    }
    commands = []
    section = scan_sections.get(scan_type, '')
    if section:
        section_started = False
        for line in markdown_content.split('\n'):
            if section in line:
                section_started = True
            elif section_started and line.startswith('### '):
                break  # End of the relevant section
            elif section_started and line.strip().startswith('* `nmap'):
                command = line.split('`')[1]
                commands.append(command)
    return commands

def main():
    args = parse_args()
    markdown_content = get_markdown_from_github(REPO_NAME, FILE_PATH, GITHUB_TOKEN)
    if markdown_content:
        commands = parse_markdown_for_commands(markdown_content, args.type)
        if commands:
            playbook_path, report_filename = generate_ansible_playbook(commands, args.targets)
            execute_ansible_playbook(playbook_path)
            convert_xml_to_json(report_filename)
        else:
            print("No commands found for the specified scan type.")
    else:
        print("Failed to retrieve or parse the markdown content from GitHub.")

    # Automatisation du lancement de attack_launcher.py après le travail principal
    print("Launching attack orchestrator...")
    subprocess.run(['python3', 'attack_launcher.py'], check=True)

if __name__ == '__main__':
    main()
