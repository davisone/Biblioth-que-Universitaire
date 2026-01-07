"""
=============================================================================
TEST DES FONCTIONS CRUD
=============================================================================

Ce fichier montre comment utiliser les fonctions CRUD avec SQLAlchemy ORM

Pour l'exécuter :
    python test_crud.py

=============================================================================
"""

import sys
import os
# Ajouter le dossier parent au path Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import get_session
from src.crud_orm import *
from src.models import Etudiant
from datetime import date


def test_crud_etudiant():
    """
    Teste les opérations CRUD sur les étudiants
    """
    print("="*60)
    print("TEST CRUD - ÉTUDIANTS")
    print("="*60)

    # Créer une session
    session = get_session()

    try:
        # ===== CREATE =====
        print("\n1️⃣ CREATE : Créer un nouvel étudiant")
        id_etudiant = create_etu(
            session,
            nom="Martin",
            prenom="Sophie",
            email="sophie.martin@univ.fr",
            date_inscription=date.today(),
            solde_amende=0
        )
        print(f"   ✅ Étudiant créé avec l'ID : {id_etudiant}")

        # ===== READ =====
        print("\n2️⃣ READ : Lire les informations de l'étudiant")
        etudiant = read_etu(session, "Martin")
        if etudiant:
            print(f"   ✅ Trouvé : {etudiant.prenom} {etudiant.nom}")
            print(f"      Email : {etudiant.email}")
            print(f"      ID : {etudiant.id_etud}")
        else:
            print("   ❌ Étudiant non trouvé")

        # ===== UPDATE =====
        print("\n3️⃣ UPDATE : Modifier le prénom")
        succes = update_etu(session, id_etudiant, "Marie")
        if succes:
            print("   ✅ Prénom modifié avec succès")
            # Vérifier la modification
            etudiant = session.query(Etudiant).get(id_etudiant)
            print(f"      Nouveau prénom : {etudiant.prenom}")
        else:
            print("   ❌ Modification échouée")

        # ===== DELETE =====
        print("\n4️⃣ DELETE : Supprimer l'étudiant")
        succes = delete_etu(session, "Martin")
        if succes:
            print("   ✅ Étudiant supprimé avec succès")
        else:
            print("   ❌ Suppression échouée")

        print("\n" + "="*60)
        print("✅ Tous les tests CRUD pour les étudiants ont réussi !")
        print("="*60)

    except Exception as e:
        print(f"\n❌ Erreur lors des tests : {e}")
        session.rollback()

    finally:
        # Toujours fermer la session
        session.close()


def test_crud_livre():
    """
    Teste les opérations CRUD sur les livres
    """
    print("\n\n")
    print("="*60)
    print("TEST CRUD - LIVRES")
    print("="*60)

    session = get_session()

    try:
        # ===== CREATE =====
        print("\n1️⃣ CREATE : Ajouter un nouveau livre")
        isbn = create_livre(
            session,
            isbn="9789999999999",
            titre="Test Python pour B3",
            editeur="Éditions Test",
            annee=2026,
            exemplaires_dispo=5
        )
        print(f"   ✅ Livre créé avec l'ISBN : {isbn}")

        # ===== READ =====
        print("\n2️⃣ READ : Lire les informations du livre")
        livre = read_livre(session, "9789999999999")
        if livre:
            print(f"   ✅ Trouvé : {livre.titre}")
            print(f"      Éditeur : {livre.editeur}")
            print(f"      Exemplaires : {livre.exemplaires_dispo}")
        else:
            print("   ❌ Livre non trouvé")

        # ===== UPDATE =====
        print("\n3️⃣ UPDATE : Modifier le nombre d'exemplaires")
        succes = update_livre(session, "9789999999999", nouveaux_exemplaires=10)
        if succes:
            print("   ✅ Livre modifié avec succès")
            livre = read_livre(session, "9789999999999")
            print(f"      Nouveaux exemplaires : {livre.exemplaires_dispo}")
        else:
            print("   ❌ Modification échouée")

        # ===== DELETE =====
        print("\n4️⃣ DELETE : Supprimer le livre")
        succes = delete_livre(session, "9789999999999")
        if succes:
            print("   ✅ Livre supprimé avec succès")
        else:
            print("   ❌ Suppression échouée")

        print("\n" + "="*60)
        print("✅ Tous les tests CRUD pour les livres ont réussi !")
        print("="*60)

    except Exception as e:
        print(f"\n❌ Erreur lors des tests : {e}")
        session.rollback()

    finally:
        session.close()


def afficher_tous_les_etudiants():
    """
    Affiche la liste de tous les étudiants
    """
    print("\n\n")
    print("="*60)
    print("LISTE DE TOUS LES ÉTUDIANTS")
    print("="*60)

    session = get_session()

    try:
        etudiants = get_all_etudiants(session)

        if etudiants:
            for etu in etudiants:
                print(f"  • {etu.nom} {etu.prenom} - {etu.email}")
            print(f"\nTotal : {len(etudiants)} étudiant(s)")
        else:
            print("  Aucun étudiant trouvé")

    except Exception as e:
        print(f"❌ Erreur : {e}")

    finally:
        session.close()


# ============================================================
#                      PROGRAMME PRINCIPAL
# ============================================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║       TEST DES FONCTIONS CRUD - BIBLIOTHÈQUE B3          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    # Lancer les tests
    test_crud_etudiant()
    test_crud_livre()
    afficher_tous_les_etudiants()

    print("\n\n✅ Tous les tests sont terminés !\n")
