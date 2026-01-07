"""
Page des amendes - Gestion des amendes étudiantes
"""
import streamlit as st
from src.utils import executer_requete_sql, convertir_en_tableau


def afficher():
    """Affiche la page de gestion des amendes"""

    st.header("💰 Gestion des amendes")

    # Requête SQL - seulement les étudiants avec amendes
    requete = """
        SELECT id_etud, nom, prenom, email, solde_amende
        FROM etudiant
        WHERE solde_amende > 0
        ORDER BY solde_amende DESC;
    """

    # Exécution
    resultat = executer_requete_sql(requete)
    tableau_amendes = convertir_en_tableau(
        resultat,
        ["ID", "Nom", "Prénom", "Email", "Montant (€)"]
    )

    if not tableau_amendes.empty:
        # Affichage du tableau
        st.dataframe(tableau_amendes, width='stretch', height=400)

        # Calcul et affichage du total
        total = executer_requete_sql(
            "SELECT SUM(solde_amende) FROM etudiant WHERE solde_amende > 0;"
        )
        st.metric(
            label="💵 Total des amendes à collecter",
            value=f"{total}€"
        )

        st.success(f"✅ {len(tableau_amendes)} étudiant(s) avec des amendes")
    else:
        st.success("🎉 Excellent ! Aucune amende en cours.")
