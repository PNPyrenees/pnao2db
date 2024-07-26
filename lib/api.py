from datetime import datetime
import requests
import yaml

from .logger import Logger


class Api:


    def __init__(self):
        """ Requete d'authentification à l'API
        Sauvearde du token sous la forme d'un header http """
        with open("config/config.yml", "r") as config_data:
            config = yaml.load(config_data, Loader=yaml.BaseLoader)

            apiUser = config["api"]["apiUser"]
            apiPassword = config["api"]["apiPassword"]

        # On ouvre une instance de logger
        self.logger = Logger()

        # Authentification 'PNAO'
        bodyContent = {'username' : apiUser, 'password': apiPassword}
        response = requests.post("https://pnao.geomatika.fr/v6/services/webservices/auth/0/", json = bodyContent)

        if response.status_code != 200:
            self.logger.logError(
                code = "100",
                message = "Erreur lors de l'authentification sur l'API PNAO",
                exception = response.json()
            )

        # Récupération du Token et construction du header
        token = response.json()['token']
        self.headers = {'Authorization': 'Bearer ' + token}


    def getZSMCoeur(self):
        """ Récupération des ZSM Coeur""" 
        responses = requests.get('https://pnao.geomatika.fr/v6/services/webservices/data/0/export_zsm_coeur', headers=self.headers)
        if responses.status_code != 200:
            self.logger.logError(
                code = "100",
                message = "Erreur lors de la récupération des données <ZSM-Coeur>",
                exception = responses.json()
            )
            return None
            
        return responses.json()


    def getZSMTampon(self):
        """ Récupération des ZSM Tampon""" 
        responses = requests.get('https://pnao.geomatika.fr/v6/services/webservices/data/0/export_zsm_tampon', headers=self.headers)
        if responses.status_code != 200:
            self.logger.logError(
                code = "100",
                message = "Erreur lors de la récupération des données <ZSM-Tampon>",
                exception = responses.json()
            )
            return None
            
        return responses.json()