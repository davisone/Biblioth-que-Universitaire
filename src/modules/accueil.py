"""
Page d'accueil - Tableau de bord
"""
import streamlit as st
from src.utils import executer_requete_sql


def afficher():
    """Affiche la page d'accueil"""

    st.header("📊 Tableau de bord - Vue d'ensemble")
    st.info("👋 Bienvenue dans le système de gestion de la bibliothèque universitaire !")

    # Statistiques principales
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        nombre_livres = executer_requete_sql("SELECT COUNT(*) FROM livre;")
        st.metric("📚 Total de livres", nombre_livres)

    with col2:
        nombre_etudiants = executer_requete_sql("SELECT COUNT(*) FROM etudiant;")
        st.metric("👨‍🎓 Total d'étudiants", nombre_etudiants)

    with col3:
        nombre_emprunts = executer_requete_sql("SELECT COUNT(*) FROM emprunt;")
        st.metric("📖 Total d'emprunts", nombre_emprunts)

    with col4:
        exemplaires_dispo = executer_requete_sql("SELECT SUM(exemplaires_dispo) FROM livre;")
        st.metric("📦 Exemplaires disponibles", exemplaires_dispo)

    st.markdown("---")

    # Informations complémentaires
    st.subheader("📌 Informations complémentaires")
    col_gauche, col_droite = st.columns(2)

    with col_gauche:
        emprunts_actifs = executer_requete_sql(
            "SELECT COUNT(*) FROM emprunt WHERE date_retour IS NULL;"
        )
        st.metric("🔄 Emprunts en cours", emprunts_actifs)

    with col_droite:
        total_amendes = executer_requete_sql(
            "SELECT COALESCE(SUM(solde_amende), 0) FROM etudiant;"
        )
        st.metric("💰 Total des amendes", f"{total_amendes}€")
