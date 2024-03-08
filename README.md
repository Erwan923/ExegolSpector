
![image](https://github.com/Erwan923/ExegolSpector/assets/82095453/43bdb0b6-50ea-4e85-85fe-b5d2fc8f3a51)


## ExegolSpector: Automatisation pour Tests d'Intrusion


## Introduction

ExegolSpector est une boite à outils de pentest conçue pour automatiser les tests d'intrusion et s'intégrer de manière fluide à des environnements conteneurisés, notamment le contenaire Exegol. (https://github.com/ThePorgs/Exegol)
Grâce à une utilisation stratégique de Python, de génération de playbook Ansible , et à une intégration poussée avec GitHub, ExegolSpector peut etre utile pour les pentesters, les participants de CTF, et les étuidiants en cybersécurité. 
ExegolSpector facilite la réalisation de scans de réseaux sur plusierus cibles, la génération dynamique de playbooks Ansible et l'exploitation de vulnérabilités de manière efficace et automatisée.

## Démarrage Rapide

 . git clone https://github.com/VotreUsername/ExegolSpector.git
 . cd ExegolSpector
 . sudo python3 ExegolSpector4.py --type advanced --targets IP
 
## Installation avec Docker

Pour simplifier le déploiement et l'utilisation d'ExegolSpector, vous pouvez le lancer dans un conteneur Docker. Voici comment procéder :

### Construire l'image Docker

Tout d'abord, construisez l'image Docker à partir du Dockerfile présent dans votre répertoire. Assurez-vous d'être dans le répertoire contenant le Dockerfile d'ExegolSpector, puis exécutez :

```bash
docker build -t exegolspector_custom
docker run -it exegolspector_custom




Pour plus de détails et pour consulter la documentation complète, visitez Documentation d'ExegolSpector.


