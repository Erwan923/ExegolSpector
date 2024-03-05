import argparse
import subprocess
import yaml
import os
import json
import xmltodict

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

def main():
    args = parse_args()
    
    # Example commands for illustration; this should be dynamically generated based on the scan type
    commands = ["nmap -sV", "nmap -A"]  # Placeholder for actual command selection logic

    playbook_path, report_filename = generate_ansible_playbook(commands, args.targets)
    execute_ansible_playbook(playbook_path)
    convert_xml_to_json(report_filename)

if __name__ == '__main__':
    main()
