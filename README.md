
![Capture d'écran 2024-03-07 041156](https://github.com/Erwan923/ExegolSpector/assets/82095453/65603ace-5433-4188-9b59-1f9314504b56)


## ExegolSpector: Automatisation pour Tests d'Intrusion

## Introduction

ExegolSpector est une boite à outils de pentest conçue pour automatiser les tests d'intrusion et s'intégrer de manière fluide à divers OS de pentest.
Une image custom avec un Dockerfile pour le contenaire Exegol à été crée dans le projet ainsi qu'un docker-compose pour une installation rapide. [Plus d'informations sur Exegol.]https://exegol.readthedocs.io/en/latest/exegol-image/tools.html

Le script Python ExegolSpector.py utilise la fonction de parsing afin de lire les différentes cheetsheet au format markdown et génère un playbook Ansible en fonction du type de scan choisi puis génère un rapport au format JSON contenant les résultat du scnan nmap. 

le script attack_orchestrtor.py lis ce JSON puis  en fonction de ports ouverts après ce scan lance les script correspondant. Le script cve_serach.py se charge de rechercher des CVE en lisant le rapport égalemment.   


ExegolSpector facilite la réalisation de scans de réseaux sur plusieurs cibles, la génération dynamique de playbooks Ansible, le recherche et l'exploitation de vulnérabilités de manière efficace et automatisée.

## Installation Rapide

Pour commencer à utiliser ExegolSpector  :

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/VotreUsername/ExegolSpector.git

2. Accédez au répertoire du projet
   ```bash
    cd ExegolSpector

3. Définir le token Github dans le script ExegolSpector.py

    ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/4218c581-91c7-49c6-8089-a1394d0b95f1)

## Démonstration sur la box Archetype de Hack the box en une seul commande

   ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/f3836208-ec4b-4dd3-a234-56d30d113db5)
   
   
1. Choix du type de scan
    ```bash
     sudo python3 ExegolSpector.py --type ['basic','advanced' ] --targets [IP]

2. Génération via les fichiers .md et lancement du Playbook Ansible intégrant les commandes nmap pour le type de scan basic (ou advanced au choix) : 

   ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/0fda5db0-ff98-4752-854f-890a2c07cf7e)


3. Rapport nmap_report.json et port ouverts :

   ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/87ba7acf-79df-4781-b905-31463e952b13)




   ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/a57407b9-bc65-4256-a3cf-ed130130add1)

   


   

   
5. Lancement automatique du script orchestrateur lançant les scripts correspondant au rapport nmap après lecture automatique :

   ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/08dd58a0-be83-4c34-b1de-6e5b84eb0b7d)





 7. Résultat du script smb_scan.sh et connexion au serveur SMB

    ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/122354a3-4519-4132-9ab2-7896f63553f5)

   

 8. Récupération des identifants dans le ficher prod.dtsConfig

    ![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/2d7dd741-98c3-4da7-9514-3d17448de6d6)

 En examinant le contenu de ce fichier de configuration, nous repérons en clair le mot de passe de l'utilisateur sql_svc ,
 qui est M3g4c0rp123 , pour l'hôte ARCHETYPE . 
   

## Fonction Automatisée de Rapport et d'Attaque

Après chaque scan, ExegolSpector effectue deux actions principales :

1.Génération de Rapport JSON : Un rapport détaillant les résultats du scan est créé en format JSON, incluant les vulnérabilités détectées.

2.Lancement Automatique des Scripts d'Attaque : Sur la base des vulnérabilités identifiées, des scripts d'attaque spécifiques sont exécutés automatiquement pour tester ces failles.

3.Génération de rapport de penstest en json ou en formrat texte avec l'impplémentation de l' IA si choisi. 

## Architecture

![Architecture](https://github.com/Erwan923/ExegolSpector/assets/82095453/145da99a-a765-49e4-86da-36c539a0801e)


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

1. En cours (Monitoring avec différents dashboard)


## wiki

1. Site en cours de construction 

## Implémentation AI 

1. fine tunning du modele Mistral 7b pour des rapport de pentsest automatquement généré.
 
## Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.

   
