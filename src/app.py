"""
Application principale - Système de Gestion de Bibliothèque Universitaire
"""

import streamlit as st
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import des différents modules de pages
from src.modules import accueil, livres, etudiants, emprunts, amendes, gestion


# ============ CONFIGURATION DE LA PAGE WEB ============
st.set_page_config(
    page_title="Bibliothèque Universitaire",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============ TITRE PRINCIPAL ============
st.title("Système de Gestion de Bibliothèque Universitaire")
st.markdown("---")


# ============ MENU DE NAVIGATION (SIDEBAR) ============
st.sidebar.title("Menu de Navigation")

# L'utilisateur choisit quelle page afficher
page_selectionnee = st.sidebar.radio(
    "Aller à :",
    [
        "Accueil",
        "Livres",
        "Étudiants",
        "Emprunts",
        "Amendes",
        "Gestion CRUD"
    ]
)
# ============ ROUTAGE VERS LA BONNE PAGE ============
if page_selectionnee == "Accueil":
    accueil.afficher()

elif page_selectionnee == "Livres":
    livres.afficher()

elif page_selectionnee == "Étudiants":
    etudiants.afficher()

elif page_selectionnee == "Emprunts":
    emprunts.afficher()

elif page_selectionnee == "Amendes":
    amendes.afficher()

elif page_selectionnee == "Gestion CRUD":
    gestion.afficher()


# ============ PIED DE PAGE ============
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>Bibliothèque Universitaire - Projet B3 Développement</p>
        <p><small>Développé avec Python, Streamlit et PostgreSQL</small></p>
    </div>
    """,
    unsafe_allow_html=True
)
