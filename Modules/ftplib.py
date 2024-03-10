import ftplib
import sys

def list_ftp_files(ftp_server):
    # Assumer des identifiants par défaut si nécessaire
    ftp_user = 'anonymous'
    ftp_password = 'anonymous'

    try:
        with ftplib.FTP(ftp_server) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_password)
            print(f"Liste des fichiers sur le serveur {ftp_server}:")
            ftp.dir()
    except ftplib.all_errors as e:
        print(f"Erreur de connexion ou de listing FTP : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ftp_server = sys.argv[1]  # Cela permet d'accepter l'adresse IP cible comme argument
        list_ftp_files(ftp_server)
    else:
        print("Usage: python3 ftplib.py <ftp_server_ip>")
