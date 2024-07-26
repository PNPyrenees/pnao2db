import psycopg2
import psycopg2.extras
import yaml

from .logger import Logger

class Database :

    def __init__(self):
        """ Initialisation de la connexion à la base de données """

        with open("config/config.yml", "r") as config_data:
            config = yaml.load(config_data, Loader=yaml.BaseLoader)

            dbName = config["database"]["dbName"]
            dbPort = str(config["database"]["dbPort"])
            dbUser = config["database"]["dbUser"]
            dbHost = config["database"]["dbHost"]
            dbPassword = config["database"]["dbPassword"]

            self.ZSMCoeurTable = config["database"]["ZSMCoeurTable"]
            self.ZSMTamponTable = config["database"]["ZSMTamponTable"]

        """ On ouvre une instance de logger """
        self.logger = Logger()

        try:
            connect_str = "dbname="+dbName+" port="+str(dbPort)+" user="+dbUser+" host="+dbHost+" password="+dbPassword
            """ Etablissement de la connexion """
            self.conn = psycopg2.connect(connect_str)
            """ Création d'un "curseur" permettant l'execution de requête """
            self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        except Exception as e:
            self.logger.logError(
                code = "000", 
                message = "Impossible de se connecter à la base de données", 
                exception = e
            )

    def close(self):
        """ Fermeture la connexion """

        self.conn.cursor().close()
        self.conn.close()

    def insertZSMTampon(self, datas):
        """ Requête d'insertion des données 
        ZSM tampon """

        # On commence par vider la table de destination
        try:
            self.cursor.execute("""DELETE FROM """ + self.ZSMTamponTable)
        except Exception as e:
            # Ecriture de l'erreur dans les logs
            self.logger.logError(
                code = "021",
                message = "Erreur lors de la réinitialisation de la table " + self.ZSMTamponTable + " en base",
                exception = e
            )

        # Puis on insère les données récupérées depuis l'API
        try:
            template="""(
                %(id_zsm_tampon)s,  
                %(code_zsm)s,  
                %(idcode_aire)s,  
                %(code_aire)s,  
                %(nom_aire)s,  
                %(actif)s,  
                %(aire_historique)s,  
                %(idespece)s,  
                %(cd_nom)s,  
                %(espece)s,  
                %(nom_latin)s,  
                %(code_dep)s,  
                %(idsite)s,  
                %(site)s,  
                %(equivalence_code_reseau)s,  
                ST_GeomFromText(%(geom_txt)s, 2154) 
            
            )"""

            psycopg2.extras.execute_values(self.cursor, """INSERT INTO """ + self.ZSMTamponTable + """ (
                    id_zsm_tampon,
                    code_zsm,
                    idcode_aire,
                    code_aire,
                    nom_aire,
                    actif,
                    aire_historique,
                    idespece,
                    cd_nom,
                    espece,
                    nom_latin,
                    code_dep,
                    idsite,
                    site,
                    equivalence_code_reseau,
                    geom
                ) 
                VALUES %s""", datas, template=template
            )

            self.conn.commit()
        except Exception as e:
            # Ecriture de l'erreur dans les logs
            self.logger.logError(
                code = "022",
                message = "Erreur de l'insertion des données ZSM-Tampon en base",
                exception = e
            )

    def insertZSMCoeur(self, datas):
        """ Requête d'insertion des données 
        ZSM coeur """

        # On commence par vider la table de destination
        try:
            self.cursor.execute("""DELETE FROM """ + self.ZSMCoeurTable)            
        except Exception as e:
            # Ecriture de l'erreur dans les logs
            self.logger.logError(
                code = "011",
                message = "Erreur lors de la réinitialisation de la table " + self.ZSMCoeurTable + " en base",
                exception = e
            )

        # Puis on insère les données récupérées depuis l'API
        try:
            template="""(
                %(id_zsm_coeur)s,  
                %(code_zsm)s,  
                %(idcode_aire)s,  
                %(code_aire)s,  
                %(nom_aire)s,  
                %(actif)s,  
                %(aire_historique)s,  
                %(idespece)s,  
                %(cd_nom)s,  
                %(espece)s,  
                %(nom_latin)s,  
                %(code_dep)s,  
                %(idsite)s,  
                %(site)s,  
                %(equivalence_code_reseau)s, 
                %(info_rap)s, 
                ST_GeomFromText(%(geom)s, 2154) 
            
            )"""

            psycopg2.extras.execute_values(self.cursor, """INSERT INTO """ + self.ZSMCoeurTable + """ (
                    id_zsm_coeur,
                    code_zsm,
                    idcode_aire,
                    code_aire,
                    nom_aire,
                    actif,
                    aire_historique,
                    idespece,
                    cd_nom,
                    espece,
                    nom_latin,
                    code_dep,
                    idsite,
                    site,
                    equivalence_code_reseau,
                    info_rap,
                    geom
                ) 
                VALUES %s""", datas, template=template
            )

            self.conn.commit()
        except Exception as e:
            # Ecriture de l'erreur dans les logs
            self.logger.logError(
                code = "012",
                message = "Erreur de l'insertion des données ZSM-Coeur en base",
                exception = e
            )
    
    