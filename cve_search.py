import json
import requests

# Remplacez ce chemin avec le chemin vers votre fichier JSON généré par ExegolSpector.py
NMAP_JSON_OUTPUT = 'nmap_report.json'

# URL de l'API CVE pour chercher des vulnérabilités
CVE_API_URL = 'https://cve.circl.lu/api/search/'

def load_nmap_report(nmap_json_path):
    with open(nmap_json_path, 'r') as file:
        return json.load(file)

def get_cve_for_service(service_name, service_version):
    # Modifier pour incorporer la version si disponible
    search_query = service_name if service_version == "" else f"{service_name}:{service_version}"
    response = requests.get(CVE_API_URL + search_query)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch CVE data for {search_query}. Status code: {response.status_code}")
        return None

def analyze_services_for_vulnerabilities(nmap_data):
    vulnerabilities_report = []
    for host in nmap_data.get('nmaprun', {}).get('host', []):
        # Assurez-vous que host['ports']['port'] est une liste
        ports = host.get('ports', {}).get('port', [])
        if isinstance(ports, dict):
            ports = [ports]
        
        for port in ports:
            service_info = port.get('service', {})
            service_name = service_info.get('@name', "")
            service_version = service_info.get('@product', "")  # Assurez-vous que c'est la clé correcte pour la version du service
            cve_data = get_cve_for_service(service_name, service_version)
            if cve_data:
                vulnerabilities_report.append({
                    'service_name': service_name,
                    'service_version': service_version,
                    'vulnerabilities': cve_data
                })
    
    return vulnerabilities_report

def save_report_to_file(report, filename="vulnerabilities_report.json"):
    with open(filename, 'w') as file:
        json.dump(report, file, indent=4)

def main():
    nmap_data = load_nmap_report(NMAP_JSON_OUTPUT)
    vulnerabilities_report = analyze_services_for_vulnerabilities(nmap_data)
    save_report_to_file(vulnerabilities_report)
    print(f"Vulnerabilities report saved to vulnerabilities_report.json")

if __name__ == "__main__":
    main()
