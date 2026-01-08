"""
Page des emprunts - Gestion des emprunts de livres
"""
import streamlit as st
from src.utils import executer_requete_sql, convertir_en_tableau


def afficher():
    """Affiche la page de gestion des emprunts"""

    st.header("Gestion des emprunts")

    # Filtre
    afficher_seulement_actifs = st.checkbox(
        "Afficher uniquement les emprunts en cours (non retournés)",
        value=True
    )

    # Requête SQL selon le filtre
    if afficher_seulement_actifs:
        # Emprunts non retournés avec JOIN
        requete = """
            SELECT
                e.id_emprunt,
                et.nom || ' ' || et.prenom AS etudiant,
                l.titre,
                e.date_emprunt,
                CURRENT_DATE - e.date_emprunt AS jours_depuis_emprunt
            FROM emprunt e
            JOIN etudiant et ON e.id_etud = et.id_etud
            JOIN livre l ON e.isbn = l.isbn
            WHERE e.date_retour IS NULL
            ORDER BY e.date_emprunt;
        """
        noms_colonnes = ["ID", "Étudiant", "Livre", "Date d'emprunt", "Depuis (jours)"]
    else:
        # Tous les emprunts
        requete = """
            SELECT
                e.id_emprunt,
                et.nom || ' ' || et.prenom AS etudiant,
                l.titre,
                e.date_emprunt,
                e.date_retour
            FROM emprunt e
            JOIN etudiant et ON e.id_etud = et.id_etud
            JOIN livre l ON e.isbn = l.isbn
            ORDER BY e.date_emprunt DESC;
        """
        noms_colonnes = ["ID", "Étudiant", "Livre", "Date d'emprunt", "Date de retour"]

    # Exécution et affichage
    resultat = executer_requete_sql(requete)
    tableau_emprunts = convertir_en_tableau(resultat, noms_colonnes)

    if not tableau_emprunts.empty:
        st.dataframe(tableau_emprunts, width='stretch', height=500)
        st.success(f"{len(tableau_emprunts)} emprunt(s) trouvé(s)")
    else:
        if afficher_seulement_actifs:
            st.info("Aucun emprunt en cours - Tous les livres ont été retournés")
        else:
            st.warning("Aucun emprunt trouvé dans la base de données")