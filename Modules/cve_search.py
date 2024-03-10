import json
import requests
import sys

CVE_API_URL = 'https://cve.circl.lu/api/search/'

def load_nmap_report(nmap_json_path):
    try:
        with open(nmap_json_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Erreur: Le fichier {nmap_json_path} n'a pas été trouvé.")
        sys.exit(1)

def get_cve_for_service(service_name):
    try:
        response = requests.get(f"{CVE_API_URL}{service_name}")
        if response.status_code == 200:
            return response.json().get('data', [])
        else:
            print(f"Échec de la récupération des données CVE pour {service_name}. Code de statut: {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de la requête de l'API CVE: {e}")
    return []

def analyze_services_for_vulnerabilities(nmap_data):
    cve_report = []
    for host in nmap_data['nmaprun']['host']:
        address = host['address']['@addr']
        ports = host['ports']['port']
        ports = ports if isinstance(ports, list) else [ports]
        for port in ports:
            service_name = port['service']['@name']
            cve_data = get_cve_for_service(service_name)
            if cve_data:
                cve_report.append({
                    'ip_address': address,
                    'port': port['@portid'],
                    'service': service_name,
                    'cve': cve_data
                })
    return cve_report

def save_report_to_file(report, filename="vulnerabilities_report.json"):
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Rapport de vulnérabilités enregistré dans {filename}.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nmap_report_path = sys.argv[1]
        nmap_data = load_nmap_report(nmap_report_path)
        cve_report = analyze_services_for_vulnerabilities(nmap_data)
        save_report_to_file(cve_report)
    else:
        print("Usage: python3 cve_search.py <chemin_vers_le_rapport_nmap_json>")
