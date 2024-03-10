import subprocess
import re
import json
import time
import os

# Configuration initiale
IMSI_CATCHER_PATH = "./IMSI-catcher"  # Chemin vers le répertoire IMSI-catcher cloné
REPORT_FILE = "gsm_interception_report.json"  # Nom du fichier de rapport

def scan_gsm_frequencies():
    print("Scanning des fréquences GSM en cours...")
    result = subprocess.check_output("grgsm_scanner", shell=True, text=True)
    frequences = re.findall(r'\b\d{3}\.\dM\b', result)
    if frequences:
        print("Fréquences trouvées : ", frequences)
    else:
        print("Aucune fréquence GSM trouvée.")
    return frequences

def intercept_gsm(frequency):
    print(f"Écoute et interception sur la fréquence {frequency}...")
    live_mon_process = subprocess.Popen(["grgsm_livemon_headless", "-f", frequency], cwd=IMSI_CATCHER_PATH)
    # Laisser un peu de temps pour que grgsm_livemon_headless démarre
    time.sleep(10)
    try:
        # Lancement du script IMSI-catcher pour capturer les IMSI
        imsi_catcher_output = subprocess.check_output(["sudo", "python", "simple_IMSI-catcher.py", "--sniff"], cwd=IMSI_CATCHER_PATH, text=True, timeout=60)
        return imsi_catcher_output
    except subprocess.TimeoutExpired:
        # Assurer l'arrêt de grgsm_livemon_headless après la capture
        live_mon_process.terminate()
        return ""

def save_report(data):
    if data:
        with open(REPORT_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Rapport enregistré dans {REPORT_FILE}")
    else:
        print("Aucune donnée à enregistrer.")

if __name__ == "__main__":
    frequences = scan_gsm_frequencies()
    if frequences:
        # Pour cet exemple, nous utilisons la première fréquence trouvée
        raw_data = intercept_gsm(frequences[0])
        if raw_data:
            # Convertir le raw_data en format JSON (implique un parsing personnalisé basé sur le format de sortie du IMSI-catcher)
            # Ceci est un exemple; vous devrez adapter cette partie pour correspondre au format exact du output
            data_to_save = {"raw_data": raw_data}
            save_report(data_to_save)
        else:
            print("Aucune donnée interceptée.")
    else:
        print("Scan des fréquences GSM n'a trouvé aucune cible.")
