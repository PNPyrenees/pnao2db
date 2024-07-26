from lib.database import Database
from lib.api import Api

def main():
    """Fonction principale de mise à jour des données GPS"""

    # Initialisation de la connexion à la base de données
    database = Database()

    # Authentification auprès de l'API (->récupération token)
    api = Api()

    # Intégration des données ZSM coeur
    ZSMCoeurdatas = api.getZSMCoeur()
    database.insertZSMCoeur(ZSMCoeurdatas)

    # Intégration des données ZSM tapon
    ZSMTampondatas = api.getZSMTampon()
    database.insertZSMTampon(ZSMTampondatas)

    # Fermeture de la connexion à la base de données
    database.close()

if __name__ == '__main__':
    main()



