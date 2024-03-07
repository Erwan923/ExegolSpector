import ftplib

def list_ftp_files():
    # définir les informations du serveur FTP
    ftp_server = '192.168.253.130'
    ftp_user = 'anonymous'
    ftp_password = 'anonymous'

    # se connecter au serveur FTP
    with ftplib.FTP(ftp_server) as ftp:
        # se connecter avec le login anonymous
        ftp.login(user=ftp_user, passwd=ftp_password)

        # afficher la liste des fichiers sur le serveur
        print("Liste des fichiers :")
        ftp.dir(".", callback=print_line)

def print_line(line):
    # afficher chaque ligne avec des informations sur le fichier
    print(line)

# lancer la fonction pour lister les fichiers du serveur FTP
list_ftp_files()
