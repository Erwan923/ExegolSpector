
![Capture d'écran 2024-03-07 041156](https://github.com/Erwan923/ExegolSpector/assets/82095453/65603ace-5433-4188-9b59-1f9314504b56)


## ExegolSpector: Automatisation pour Tests d'Intrusion

## Introduction

ExegolSpector est une boite à outils de pentest conçue pour automatiser les tests d'intrusion et s'intégrer de manière fluide à des environnements conteneurisés, notamment le contenaire Exegol et ses différentes outils. [Plus d'informations sur Exegol.]https://exegol.readthedocs.io/en/latest/exegol-image/tools.html

Grâce à plusieurs scripts Python, de génération de playbook Ansible, et à une intégration poussée avec GitHub, ExegolSpector peut être utile pour les débutants en cyber, les participants de CTF, et les étudiants en cybersécurité.

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
    
## Fonction Automatisée de Rapport et d'Attaque

Après chaque scan, ExegolSpector effectue deux actions principales :

1.Génération de Rapport JSON : Un rapport détaillant les résultats du scan est créé en format JSON, incluant les vulnérabilités détectées.

2.Lancement Automatique des Scripts d'Attaque : Sur la base des vulnérabilités identifiées, des scripts d'attaque spécifiques sont exécutés automatiquement pour tester ces failles.

## Installation avec Docker

1. Construire l'image Docker
   ```bash
   docker build -t exegolspector_custom .
2. Lancer le conteneur
   ```bash
   docker run -it exegolspector_custom
3. Pour plus de persitantce et de modification
     ```bash
     docker-compose up
4. Et pour exécuter ExegolSpector dans ce conteneur en mode interactif
   ```bash
   docker-compose exec exegolspector bash

## Tableau de suivi en temps réel

1. GUI web avec différents dashboard permettant d'avoir une meilleur visualisation des rapports de scan


## Interface graphique

## Implémentation AI 

1. Une impkémentation de l' IA au projet est possible en démarrant le projet avec la commande ci dessus : 


2. Des rapport de pentsest automatquement généré peuvent etre retroouvé égaemment en effectuant cette commande : 
 
## Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.

   
