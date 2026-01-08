"""
Page de gestion - CRUD complet (Create, Read, Update, Delete)
"""
import streamlit as st
from datetime import date
from src.database import get_session
from src.crud_orm import (
    create_livre, update_livre, delete_livre, get_all_livres,
    create_etu, update_etu, delete_etu, get_all_etudiants,
    create_emprunt, retourner_livre, get_emprunts_actifs
)


def afficher():
    """Affiche la page de gestion CRUD"""

    st.header("Gestion CRUD - Créer, Modifier, Supprimer")

    # Choix de l'entité à gérer
    entite = st.selectbox(
        "Que voulez-vous gérer ?",
        ["Livres", "Étudiants", "Emprunts"]
    )

    st.markdown("---")

    if entite == "Livres":
        gerer_livres()
    elif entite == "Étudiants":
        gerer_etudiants()
    elif entite == "Emprunts":
        gerer_emprunts()


def gerer_livres():
    """Gestion CRUD des livres"""

    operation = st.radio("Opération", ["Ajouter", "Modifier", "Supprimer"], horizontal=True)

    st.markdown("---")

    if operation == "Ajouter":
        st.subheader("Ajouter un nouveau livre")

        with st.form("form_ajouter_livre"):
            isbn = st.text_input("ISBN *", placeholder="Ex: 978-2-1234-5680-3")
            titre = st.text_input("Titre *", placeholder="Ex: Python pour les nuls")
            editeur = st.text_input("Éditeur *", placeholder="Ex: Eyrolles")
            annee = st.number_input("Année *", min_value=1900, max_value=2030, value=2024)
            exemplaires = st.number_input("Nombre d'exemplaires *", min_value=1, value=1)

            submitted = st.form_submit_button("Ajouter le livre")

            if submitted:
                if not isbn or not titre or not editeur:
                    st.error("Tous les champs marqués * sont obligatoires !")
                else:
                    try:
                        session = get_session()
                        create_livre(session, isbn, titre, editeur, annee, exemplaires)
                        session.close()
                        st.success(f"Livre '{titre}' ajouté avec succès !")
                    except Exception as e:
                        st.error(f"Erreur : {str(e)}")

    elif operation == "Modifier":
        st.subheader("Modifier un livre")

        session = get_session()
        livres = get_all_livres(session)
        session.close()

        if not livres:
            st.warning("Aucun livre dans la base de données.")
            return

        livre_choisi = st.selectbox(
            "Sélectionner un livre",
            options=[(l.isbn, f"{l.titre} ({l.isbn})") for l in livres],
            format_func=lambda x: x[1]
        )

        if livre_choisi:
            with st.form("form_modifier_livre"):
                nouveau_titre = st.text_input("Nouveau titre (optionnel)")
                nouveaux_exemplaires = st.number_input("Nouveau nombre d'exemplaires (optionnel)", min_value=0)

                submitted = st.form_submit_button("Modifier")

                if submitted:
                    try:
                        session = get_session()
                        update_livre(
                            session,
                            livre_choisi[0],
                            nouveau_titre if nouveau_titre else None,
                            nouveaux_exemplaires if nouveaux_exemplaires > 0 else None
                        )
                        session.close()
                        st.success("Livre modifié avec succès !")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erreur : {str(e)}")

    else:  # Supprimer
        st.subheader("Supprimer un livre")
        st.warning("Attention : Cette action est irréversible !")

        session = get_session()
        livres = get_all_livres(session)
        session.close()

        if not livres:
            st.warning("Aucun livre dans la base de données.")
            return

        livre_choisi = st.selectbox(
            "Sélectionner un livre à supprimer",
            options=[(l.isbn, f"{l.titre} ({l.isbn})") for l in livres],
            format_func=lambda x: x[1]
        )

        if livre_choisi and st.button("Confirmer la suppression", type="primary"):
            try:
                session = get_session()
                delete_livre(session, livre_choisi[0])
                session.close()
                st.success("Livre supprimé !")
                st.rerun()
            except Exception as e:
                st.error(f"Erreur : {str(e)}")


def gerer_etudiants():
    """Gestion CRUD des étudiants"""

    operation = st.radio("Opération", ["Ajouter", "Modifier", "Supprimer"], horizontal=True)

    st.markdown("---")

    if operation == "Ajouter":
        st.subheader("Ajouter un nouvel étudiant")

        with st.form("form_ajouter_etudiant"):
            nom = st.text_input("Nom *", placeholder="Ex: Dupont")
            prenom = st.text_input("Prénom *", placeholder="Ex: Jean")
            email = st.text_input("Email *", placeholder="Ex: jean.dupont@univ.fr")
            date_inscription = st.date_input("Date d'inscription", value=date.today())
            solde_amende = st.number_input("Solde amende", min_value=0.0, value=0.0, step=0.5)

            submitted = st.form_submit_button("Ajouter l'étudiant")

            if submitted:
                if not nom or not prenom or not email:
                    st.error("Tous les champs marqués * sont obligatoires !")
                else:
                    try:
                        session = get_session()
                        create_etu(session, nom, prenom, email, date_inscription, solde_amende)
                        session.close()
                        st.success(f"Étudiant {prenom} {nom} ajouté avec succès !")
                    except Exception as e:
                        st.error(f"Erreur : {str(e)}")

    elif operation == "Modifier":
        st.subheader("Modifier un étudiant")
        st.info("Actuellement, seul le prénom peut être modifié")

        session = get_session()
        etudiants = get_all_etudiants(session)
        session.close()

        if not etudiants:
            st.warning("Aucun étudiant dans la base de données.")
            return

        etudiant_choisi = st.selectbox(
            "Sélectionner un étudiant",
            options=[(e.id_etud, f"{e.nom} {e.prenom} ({e.email})") for e in etudiants],
            format_func=lambda x: x[1]
        )

        if etudiant_choisi:
            with st.form("form_modifier_etudiant"):
                nouveau_prenom = st.text_input("Nouveau prénom *")

                submitted = st.form_submit_button("Modifier")

                if submitted:
                    if not nouveau_prenom:
                        st.error("Le nouveau prénom est obligatoire !")
                    else:
                        try:
                            session = get_session()
                            update_etu(session, etudiant_choisi[0], nouveau_prenom)
                            session.close()
                            st.success("Étudiant modifié avec succès !")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Erreur : {str(e)}")

    else:  # Supprimer
        st.subheader("Supprimer un étudiant")
        st.warning("Attention : Cette action est irréversible !")

        session = get_session()
        etudiants = get_all_etudiants(session)
        session.close()

        if not etudiants:
            st.warning("Aucun étudiant dans la base de données.")
            return

        etudiant_choisi = st.selectbox(
            "Sélectionner un étudiant à supprimer",
            options=[(e.nom, f"{e.nom} {e.prenom} ({e.email})") for e in etudiants],
            format_func=lambda x: x[1]
        )

        if etudiant_choisi and st.button("Confirmer la suppression", type="primary"):
            try:
                session = get_session()
                delete_etu(session, etudiant_choisi[0])
                session.close()
                st.success("Étudiant supprimé !")
                st.rerun()
            except Exception as e:
                st.error(f"Erreur : {str(e)}")


def gerer_emprunts():
    """Gestion CRUD des emprunts"""

    operation = st.radio("Opération", ["Créer un emprunt", "Retourner un livre"], horizontal=True)

    st.markdown("---")

    if operation == "Créer un emprunt":
        st.subheader("Créer un nouvel emprunt")

        session = get_session()
        etudiants = get_all_etudiants(session)
        livres = [l for l in get_all_livres(session) if l.exemplaires_dispo > 0]
        session.close()

        if not etudiants:
            st.warning("Aucun étudiant dans la base de données.")
            return

        if not livres:
            st.warning("Aucun livre disponible pour l'emprunt.")
            return

        with st.form("form_emprunt"):
            etudiant_choisi = st.selectbox(
                "Étudiant *",
                options=[(e.id_etud, f"{e.nom} {e.prenom}") for e in etudiants],
                format_func=lambda x: x[1]
            )

            livre_choisi = st.selectbox(
                "Livre *",
                options=[(l.isbn, f"{l.titre} ({l.exemplaires_dispo} dispo)") for l in livres],
                format_func=lambda x: x[1]
            )

            submitted = st.form_submit_button("Créer l'emprunt")

            if submitted:
                try:
                    session = get_session()
                    create_emprunt(session, etudiant_choisi[0], livre_choisi[0])
                    session.close()
                    st.success("Emprunt créé avec succès !")
                except Exception as e:
                    st.error(f"Erreur : {str(e)}")

    else:  # Retourner un livre
        st.subheader("Retourner un livre emprunté")

        session = get_session()
        emprunts_actifs = get_emprunts_actifs(session)

        if not emprunts_actifs:
            st.info("Aucun emprunt en cours ! Tous les livres ont été retournés.")
            session.close()
            return

        # Afficher les emprunts actifs avec détails
        emprunts_details = []
        for emp in emprunts_actifs:
            emprunts_details.append((
                emp.id_emprunt,
                f"ID {emp.id_emprunt} - {emp.etudiant.nom} {emp.etudiant.prenom} - {emp.livre.titre}"
            ))

        session.close()

        emprunt_choisi = st.selectbox(
            "Sélectionner un emprunt",
            options=emprunts_details,
            format_func=lambda x: x[1]
        )

        if emprunt_choisi and st.button("Confirmer le retour", type="primary"):
            try:
                session = get_session()
                retourner_livre(session, emprunt_choisi[0])
                session.close()
                st.success("Livre retourné avec succès !")
                st.rerun()
            except Exception as e:
                st.error(f"Erreur : {str(e)}")
