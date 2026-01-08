from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les informations de connexion depuis .env
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'bibliothequeuniv')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')

# Créer l'URL de connexion PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def get_engine():
    """
    Crée et retourne le moteur de base de données SQLAlchemy
    Le moteur gère la connexion à PostgreSQL
    """
    engine = create_engine(
        DATABASE_URL,
        echo=False  # Mettre True pour voir les requêtes SQL dans la console
    )
    return engine

#    Crée et retourne une session SQLAlchemy
def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
