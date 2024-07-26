# pnao2db
Script Python permettant d'automatiser la récupération des données Rapace-ZSM (coeur et tampon) depuis l'application PNAO de Geomatika à travers l'API V6

# Fonctionnement général
- Utilisation de l'APi pour l'authentification
- Téléchargement des données ZSM coeur et tampon
- Intégration des ZSM dans la base de données (annule et remplace)

**En cas d'erreur lors de l'exécution du script, un mail sera envoyé (voir configuration)**

# Environnement
Le script a été réalisé sous Ubuntu 20.04 et développé en Python3 avec une base de données est PostgreSQL 10 et l'extension PostGIS.

D'autres configurations doivent pouvoir correspondre mais reste à tester

# Récupération des codes sources
Récupérer les codes sources avec git :
```sh
$ git clone https://github.com/PNPyrenees/pnao2db.git
```

# Installation
 - Adapter puis exécuter le script d'initialisation de la base de données (install/install_db.sql)
 - Créer un environnement virtuel python
```sh
$ cd <pathTo>/pnao2db
$ python3 -m venv venv
```
 - Installer les dépendances Python
```sh
$ source venv/bin/activate
(venv) $ pip install -r install/requirements.txt
(venv) $ deactivate
```

 - Initialisation du fichier de logs
```sh
$ mkdir log
$ touch log.pnao2db.log
```
 
# Configuration
 - Copier le fichier config/config.yml.default en le renommant config.yml
```sh
$ cp config/config.yml.default config/config.yml
```
 - éditer le fichier config.yml en renseignant chacun des paramètres
```yaml
# YAML
database:
    dbHost: 
    dbName: 
    dbPort: 
    dbUser: 
    dbPassword: 
api:
    apiUser: 
    apiPassword: 
mail:
    mailHost: 
    mailPort: 
    mailId: 
    mailPass: 
    mailDest:
log:
    logFile: log/pnao2db.log
```

# Automatisation
Modifier le script pnao2db.sh de sorte que le chemin vers le dossier du projet corresponde à votre environnement local (ligne 5)

Ensuite, automatiser l'exécution du script en programmant une tâche avec cron
```
$ crontab -e 
```

Exemple d'une configuration cron pour la récupération quotidienne des données à 02h00 
```sh
00 02  * * * /<PathTo>/pnao2db.sh
```
Le chemin doit être en absolu.

#License
----
 - OpenSource - GPL-3.0
 
<a href="http://www.pyrenees-parcnational.fr" target="_blank"><img align="right" src="https://user-images.githubusercontent.com/85548796/134628003-895ecb51-fab1-4993-9cb9-53c3ea52d58b.png" alt="drawing" height="60"/></a>

[Geomatika]: <https://www.geomatika.fr/>
[PNAO]: https://pnao.geomatika.fr/
