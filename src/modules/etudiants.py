"""
Page des étudiants - Liste et gestion
"""
import streamlit as st
from src.utils import executer_requete_sql, convertir_en_tableau


def afficher():
    """Affiche la page de la liste des étudiants"""

    st.header("Liste des étudiants")

    # Filtre
    afficher_seulement_amendes = st.checkbox(
        "Afficher uniquement les étudiants avec des amendes",
        value=False
    )

    # Requête SQL selon le filtre
    if afficher_seulement_amendes:
        requete = """
            SELECT id_etud, nom, prenom, email, solde_amende
            FROM etudiant
            WHERE solde_amende > 0
            ORDER BY solde_amende DESC;
        """
        noms_colonnes = ["ID", "Nom", "Prénom", "Email", "Amende (€)"]
    else:
        requete = """
            SELECT id_etud, nom, prenom, email, date_inscription, solde_amende
            FROM etudiant
            ORDER BY nom, prenom;
        """
        noms_colonnes = ["ID", "Nom", "Prénom", "Email", "Date inscription", "Amende (€)"]

    # Exécution et affichage
    resultat = executer_requete_sql(requete)
    tableau_etudiants = convertir_en_tableau(resultat, noms_colonnes)

    if not tableau_etudiants.empty:
        st.dataframe(tableau_etudiants, width='stretch', height=500)
        st.success(f"{len(tableau_etudiants)} étudiant(s) trouvé(s)")
    else:
        st.warning("Aucun étudiant trouvé")
