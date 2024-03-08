# Utilisation d'une image Exegol existante comme base
FROM exegolcommunity/exegol:latest

# Installation de Git, Python3, et Ansible pour permettre la personnalisation et l'automatisation
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    ansible \
 && rm -rf /var/lib/apt/lists/*


ARG GITHUB_REPO=https://github.com/Erwan923/ExegolSpector.git
ARG GITHUB_BRANCH=main

RUN git clone -b ${GITHUB_BRANCH} ${GITHUB_REPO} /opt/ExegolSpector

# Installation des dépendances Python à partir de requirements.txt du dépôt cloné
RUN if [ -f /opt/ExegolSpector/requirements.txt ]; then pip3 install -r /opt/ExegolSpector/requirements.txt; fi


CMD ["/bin/bash"]

