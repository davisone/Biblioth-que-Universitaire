"""
Fonctions utilitaires pour l'application Streamlit
"""
import subprocess
import pandas as pd


def executer_requete_sql(requete_sql):
    """
    Exécute une requête SQL via Docker

    Paramètres:
        requete_sql (str): La requête SQL

    Retourne:
        str: Le résultat de la requête
    """
    try:
        commande = [
            "docker", "exec", "postgres-biblio",
            "psql", "-U", "postgres", "-d", "bibliothequeuniv",
            "-t", "-A", "-c", requete_sql
        ]

        resultat = subprocess.run(
            commande,
            capture_output=True,
            text=True,
            check=True
        )

        return resultat.stdout.strip()

    except Exception as erreur:
        return f"Erreur: {str(erreur)}"


def convertir_en_tableau(texte_resultat, noms_colonnes):
    """
    Convertit le résultat SQL en DataFrame pandas

    Paramètres:
        texte_resultat (str): Le résultat SQL brut
        noms_colonnes (list): Les noms des colonnes

    Retourne:
        DataFrame: Tableau pandas
    """
    if not texte_resultat or "Erreur" in texte_resultat:
        return pd.DataFrame()

    lignes = texte_resultat.strip().split('\n')
    donnees = []

    for ligne in lignes:
        if ligne:
            colonnes = ligne.split('|')
            donnees.append(colonnes)

    if not donnees:
        return pd.DataFrame()

    return pd.DataFrame(donnees, columns=noms_colonnes)
