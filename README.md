## ExegolSpector: Automatisation pour Tests d'Intrusion

## Introduction

ExegolSpector est une boite à outils de pentest conçue pour automatiser les tests d'intrusion et s'intégrer de manière fluide à des environnements conteneurisés, notamment le contenaire Exegol. [Plus d'informations sur Exegol.](https://github.com/ThePorgs/Exegol)

Grâce à une utilisation stratégique de Python, de génération de playbook Ansible, et à une intégration poussée avec GitHub, ExegolSpector peut être utile pour les pentesters, les participants de CTF, et les étudiants en cybersécurité.

ExegolSpector facilite la réalisation de scans de réseaux sur plusieurs cibles, la génération dynamique de playbooks Ansible et l'exploitation de vulnérabilités de manière efficace et automatisée.

## Démarrage Rapide

Pour commencer à utiliser ExegolSpector  :

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/VotreUsername/ExegolSpector.git

2. Accédez au répertoire du projet
   ```bash
    cd ExegolSpector
3. Choix du type de scan
    ```bash
     sudo python3 ExegolSpector.py --type [basic', 'discovery', 'advanced', 'port', 'version', 'aggressive ] --targets [IP]

