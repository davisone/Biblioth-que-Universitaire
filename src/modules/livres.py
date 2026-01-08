"""
Page des livres - Catalogue
"""
import streamlit as st
from src.utils import executer_requete_sql, convertir_en_tableau


def afficher():
    """Affiche la page du catalogue des livres"""

    st.header("Catalogue des livres")

    # Case à cocher pour filtrer les livres disponibles
    afficher_seulement_disponibles = st.checkbox(
        "Afficher uniquement les livres disponibles (exemplaires > 0)",
        value=False
    )

    # Requête SQL selon le filtre
    if afficher_seulement_disponibles:
        requete = """
            SELECT isbn, titre, editeur, annee, exemplaires_dispo
            FROM livre
            WHERE exemplaires_dispo > 0
            ORDER BY titre;
        """
    else:
        requete = """
            SELECT isbn, titre, editeur, annee, exemplaires_dispo
            FROM livre
            ORDER BY titre;
        """

    resultat = executer_requete_sql(requete)

    # Conversion en tableau
    tableau_livres = convertir_en_tableau(
        resultat,
        ["ISBN", "Titre", "Éditeur", "Année", "Exemplaires disponibles"]
    )

    # Affichage
    if not tableau_livres.empty:
        st.dataframe(
            tableau_livres,
            width='stretch',
            height=500
        )
        st.success(f"{len(tableau_livres)} livre(s) trouvé(s)")
    else:
        st.warning("Aucun livre trouvé")
