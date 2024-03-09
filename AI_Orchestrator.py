import requests
import base64
import json
import openai
import os
import subprocess
from dotenv import load_dotenv

# Charger les variables d'environnement, incluant OPENAI_API_KEY et GITHUB_TOKEN
load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = 'votre_nom_utilisateur/votre_nom_depot'
FILE_PATH = 'chemin/vers/cheatsheet.md'
NMAP_JSON_OUTPUT = 'nmap_report.json'
CVE_API_URL = 'https://cve.circl.lu/api/search/'
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_markdown_from_github():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    api_url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        file_content_base64 = response.json()['content']
        markdown_content = base64.b64decode(file_content_base64).decode('utf-8')
        return markdown_content
    else:
        print(f"Failed to fetch file from GitHub. Status Code: {response.status_code}")
        return None

def parse_markdown_for_commands(markdown_content):
    # Cette fonction doit être implémentée en fonction de la structure de votre cheatsheet
    # Pour cet exemple, supposons qu'elle retourne un dictionnaire de commandes
    return {"example_service": "example_command"}

def load_nmap_report():
    with open(NMAP_JSON_OUTPUT, 'r') as file:
        return json.load(file)

def get_cve_for_service(service_name, service_version=""):
    search_query = service_name if not service_version else f"{service_name}:{service_version}"
    response = requests.get(f"{CVE_API_URL}{search_query}")
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Failed to fetch CVE data for {search_query}. Status code: {response.status_code}")
        return []

def consult_chatgpt_for_action(service_name, vulnerabilities, commands):
    prompt = f"Given a service '{service_name}' with vulnerabilities {vulnerabilities}, what attack should be performed? Available commands: {commands}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    advice = response.choices[0].text.strip()
    print(f"ChatGPT recommends: {advice}")
    return advice

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed command: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}. Error: {e}")

def main():
    markdown_content = get_markdown_from_github()
    commands = parse_markdown_for_commands(markdown_content)
    nmap_data = load_nmap_report()
    
    for host in nmap_data.get("nmaprun", {}).get("host", []):
        service_name = host.get("service", {}).get("@name", "")
        service_version = host.get("service", {}).get("@version", "")
        vulnerabilities = get_cve_for_service(service_name, service_version)
        
        if vulnerabilities:
            advice = consult_chatgpt_for_action(service_name, vulnerabilities, commands)
            if advice in commands:
                execute_command(commands[advice])
            else:
                print(f"No executable command found for advice: {advice}")
        else:
            print(f"No vulnerabilities found for service: {service_name}")

if __name__ == "__main__":
    main()
