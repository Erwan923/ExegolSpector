
![Capture d'écran 2024-03-07 041156](https://github.com/Erwan923/ExegolSpector/assets/82095453/65603ace-5433-4188-9b59-1f9314504b56)


## ExegolSpector: Automatisation pour Tests d'Intrusion

## Introduction

ExegolSpector est une boite à outils de pentest conçue pour automatiser les tests d'intrusion et s'intégrer de manière fluide à divers OS de pentest.
Une image custom avec un Dockerfile pour le contenaire Exegol à été crée dans le projet ainsi qu'un docker-compose pour une installation rapide. [Plus d'informations sur Exegol.]https://exegol.readthedocs.io/en/latest/exegol-image/tools.html

Le script Python ExegolSpector.py utilise la fonction de parsing afin de lire les différentes cheetsheet au format markdown et génère un playbook Ansible en fonction du type de scan choisi puis génère un rapport au format JSON contenant les résultat du scnan nmap. 

le script attack_orchestrtor.py lis ce JSON puis  en fonction de ports ouverts après ce scan cherche les CVE dans la base de donnée de OWASPet lance les script correspondant grace au module subprocess. 


ExegolSpector facilite la réalisation de scans de réseaux sur plusieurs cibles, la génération dynamique de playbooks Ansible et l'exploitation de vulnérabilités de manière efficace et automatisée.

## Démarrage Rapide

Pour commencer à utiliser ExegolSpector  :

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/VotreUsername/ExegolSpector.git

2. Accédez au répertoire du projet
   ```bash
    cd ExegolSpector

3. Définir le token Github dans le script ExegolSpector.py

![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/c7005740-36a0-4680-baed-6a0c949a94ee)

   
4. Choix du type de scan
    ```bash
     sudo python3 ExegolSpector.py --type [basic', 'discovery', 'advanced', 'port', 'version', 'aggressive ] --targets [IP]

4. Lancement du Playbook Ansible intégrant les commandes nmap pour le type de scan advanced : 

![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/f863241c-18e3-4347-b433-06a8e2b9fad5)

5. Génération du rapport en format JSON :
   
7. Lancement automatique du script orchestrateur recherchant les CVE ainsi que le trype de script correspondant :
   
   

## Fonction Automatisée de Rapport et d'Attaque

Après chaque scan, ExegolSpector effectue deux actions principales :

1.Génération de Rapport JSON : Un rapport détaillant les résultats du scan est créé en format JSON, incluant les vulnérabilités détectées.

2.Lancement Automatique des Scripts d'Attaque : Sur la base des vulnérabilités identifiées, des scripts d'attaque spécifiques sont exécutés automatiquement pour tester ces failles.

3.Génération de rapport de penstest en json ou en formrat texte avec l'impplémentation de l' IA si choisi. 

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

1. Monitoring avec différents dashboard


## wiki

## Implémentation AI 

1. Une implémentation de l' IA au projet est possible (testé avec l' API gpt ou avec Mistral en local) en démarrant le projet avec la commande ci dessus : 


2. Des rapport de pentsest automatquement généré peuvent etre retroouvé égaemment en effectuant cette commande : 
 
## Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.

   
