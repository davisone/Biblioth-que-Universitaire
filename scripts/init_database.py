"""
=============================================================================
INITIALISATION DE LA BASE DE DONNÉES
=============================================================================

Ce script crée les tables et insère des données de test

=============================================================================
"""

import sys
import os
# Ajouter le dossier parent au path Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_engine, get_session
from src.models import Base, Etudiant, Livre, Emprunt
from src.crud_orm import *
from datetime import date


def creer_tables():
    """
    Crée toutes les tables dans la base de données
    """
    print("Création des tables...")
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Tables créées avec succès !")


def inserer_donnees_test():
    """
    Insère des données de test dans la base
    """
    print("\nInsertion des données de test...")
    session = get_session()

    try:
        # ===== ÉTUDIANTS =====
        print("\nAjout des étudiants...")
        etudiants_data = [
            ("Davison", "Evan", "evan.davison@supdevinci-edu.fr"),
            ("Bernard", "Thomas", "thomas.bernard@univ.fr"),
            ("Dubois", "Emma", "emma.dubois@univ.fr"),
            ("Petit", "Lucas", "lucas.petit@univ.fr"),
            ("Robert", "Chloé", "chloe.robert@univ.fr"),
        ]

        for nom, prenom, email in etudiants_data:
            create_etu(session, nom, prenom, email, date.today(), 0)
            print(f"   {prenom} {nom}")

        # ===== LIVRES =====
        print("\nAjout des livres...")
        livres_data = [
            ("9782212678529", "Clean Code", "Pearson", 2008, 3),
            ("9781449355739", "Learning Python", "O'Reilly", 2013, 2),
            ("9780134685991", "Effective Java", "Addison-Wesley", 2018, 2),
            ("9781617294945", "Spring in Action", "Manning", 2020, 4),
            ("9780135957059", "The Pragmatic Programmer", "Addison-Wesley", 2019, 5),
        ]

        for isbn, titre, editeur, annee, exemplaires in livres_data:
            create_livre(session, isbn, titre, editeur, annee, exemplaires)
            print(f"   {titre}")

        print("\nDonnées insérées avec succès !")

    except Exception as e:
        print(f"Erreur : {e}")
        session.rollback()

    finally:
        session.close()


if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     INITIALISATION DE LA BASE DE DONNÉES - B3            ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    creer_tables()
    inserer_donnees_test()

    print("\nInitialisation terminée !\n")
