import requests
import base64
import json

# Configuration GitHub
GITHUB_TOKEN = 'VOTRE_TOKEN_GITHUB'
REPO_NAME = 'VotreNomUtilisateur/VotreRepo'
FILE_PATH = 'Empire.md'  # Chemin de la cheatsheet Empire sur GitHub

# Configuration Empire
EMPIRE_API_URL = "http://localhost:1337/api/"
EMPIRE_USERNAME = "empireadmin"
EMPIRE_PASSWORD = "password"

def get_api_token():
    """Authentification à l'API d'Empire et récupération du token."""
    auth_url = f"{EMPIRE_API_URL}admin/login"
    response = requests.post(auth_url, json={"username": EMPIRE_USERNAME, "password": EMPIRE_PASSWORD})
    response.raise_for_status()  # Assurez-vous que la requête a réussi
    return response.json()['token']

def execute_empire_action(api_token, action_type, action_details):
    """Exécute une action spécifique dans Empire basée sur la cheatsheet."""
    headers = {"Authorization": f"Bearer {api_token}"}
    url = f"{EMPIRE_API_URL}{action_type}"
    
    response = requests.post(url, headers=headers, json=action_details)
    if response.status_code == 200:
        print(f"Successfully executed {action_type}: {response.json()}")
    else:
        print(f"Failed to execute {action_type}. Status Code: {response.status_code}")

def fetch_cheatsheet_from_github():
    """Récupère la cheatsheet Empire depuis GitHub."""
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

def interpret_cheatsheet(cheatsheet_content, api_token):
    """Interprète la cheatsheet et exécute les actions correspondantes."""
    # Cette fonction doit être adaptée pour parser votre format spécifique de cheatsheet
    # Pour l'exemple, on suppose qu'elle contient des blocs JSON avec des actions Empire
    try:
        actions = json.loads(cheatsheet_content)
        for action_type, action_details in actions.items():
            execute_empire_action(api_token, action_type, action_details)
    except json.JSONDecodeError:
        print("Failed to decode cheatsheet content.")

def main():
    api_token = get_api_token()
    cheatsheet_content = fetch_cheatsheet_from_github()
    if cheatsheet_content:
        interpret_cheatsheet(cheatsheet_content, api_token)

if __name__ == "__main__":
    main()
