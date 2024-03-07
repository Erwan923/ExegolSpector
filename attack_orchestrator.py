import json
import subprocess

# Définition des scripts d'attaque pour chaque service/port détecté
attacks = {
    80: "python3 fuzzing.py",
    443: "python3 web_extract.py",
    21: "python3 ftplib.py",
    445: "./SMBPortAttack.sh"
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
        if not isinstance(targets, list):  # Assurer que targets est une liste
            targets = [targets]
        for target in targets:
            address = target.get('address', {}).get('@addr', '')
            open_ports = [int(port.get('@portid')) for port in target.get('ports', {}).get('port', []) if port.get('state', {}).get('@state') == 'open']
            for port in open_ports:
                if port in attacks:
                    execute_attack(attacks[port], address)

if __name__ == "__main__":
    report_path = 'nmap_report.json'
    analyze_report_and_launch_attacks(report_path)
