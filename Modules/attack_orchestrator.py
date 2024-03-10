import json
import subprocess

# Définition des scripts d'attaque pour chaque service/port détecté
attacks = {
    80: "python3 Modules/fuzzing.py",
    443: "python3 Modules/web_extract.py",
    21: "python3 Modules/ftplib.py",
    445: "./Modules/SMBPortAttack.sh"
}

def execute_attack(script, target_ip):
    try:
        print(f"Executing attack: {script} against {target_ip}")
        subprocess.run(f"{script} {target_ip}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute attack on {target_ip}: {e}")

def analyze_report_and_launch_attacks(report_path):
    with open(report_path, 'r') as file:
        data = json.load(file)
        targets = data.get('nmaprun', {}).get('host', [])
        if not isinstance(targets, list):
            targets = [targets]
        for target in targets:
            address = target.get('address', {}).get('@addr', '')
            open_ports = [int(port.get('@portid')) for port in target.get('ports', {}).get('port', []) if port.get('state', {}).get('@state') == 'open']
            for port in open_ports:
                if port in attacks:
                    execute_attack(attacks[port], address)
    # Après avoir lancé toutes les attaques, lancez la recherche de CVE
    launch_cve_search(report_path)

def launch_cve_search(nmap_json_path):
    # Assurez-vous que le chemin vers cve_search.py est correct
    cve_search_script = './Modules/cve_search.py'
    try:
        subprocess.run(['python3', cve_search_script, nmap_json_path], check=True)
        print("CVE search completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to complete CVE search: {e}")

if __name__ == "__main__":
    report_path = '../nmap_report.json'
    analyze_report_and_launch_attacks(report_path)
