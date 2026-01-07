from .models import Etudiant, Livre, Emprunt
from datetime import date

# ============================================================
#                   CRUD POUR LES Etudiants
# ============================================================

def create_etu(session, nom, prenom, email, date_inscription, solde_amende):

def read_etu(session, nom):

return session.query(Etudiant).filter_by(nom=nom).first()

def update_etu(session, id_etud, nouveau_prenom):
    
etu = session.query(Etudiant).get(id_etud)

    if etu:
        # On modifie le prénom
        etu.prenom = nouveau_prenom
        # On enregistre
        session.commit()
        return True

    return False

def delete_etu(session, nom):
   
    # On cherche l'étudiant
    etu = read_etu(session, nom)

    if etu:
        # On le supprime
        session.delete(etu)
        session.commit()
        return True

    return False


# ============================================================
#                   CRUD POUR LES LIVRES
# ============================================================

def create_livre(session, isbn, titre, editeur, annee, exemplaires_dispo):
    
    livre = Livre(
        isbn=isbn,
        titre=titre,
        editeur=editeur,
        annee=annee,
        exemplaires_dispo=exemplaires_dispo
    )

    session.add(livre)
    session.commit()

    return livre.isbn


def read_livre(session, isbn):
    
    return session.query(Livre).filter_by(isbn=isbn).first()


def update_livre(session, isbn, nouveau_titre=None, nouveaux_exemplaires=None):
    
    livre = session.query(Livre).get(isbn)

    if livre:
        if nouveau_titre:
            livre.titre = nouveau_titre
        if nouveaux_exemplaires is not None:
            livre.exemplaires_dispo = nouveaux_exemplaires

        session.commit()
        return True

    return False


def delete_livre(session, isbn):
    
    livre = read_livre(session, isbn)

    if livre:
        session.delete(livre)
        session.commit()
        return True

    return False


# ============================================================
#                  CRUD POUR LES EMPRUNTS
# ============================================================

def create_emprunt(session, id_etud, isbn):
    
    emprunt = Emprunt(
        id_etud=id_etud,
        isbn=isbn,
        date_emprunt=date.today(),
        amende=0
    )

    session.add(emprunt)

    # Diminuer le nombre d'exemplaires disponibles
    livre = read_livre(session, isbn)
    if livre:
        livre.exemplaires_dispo -= 1

    session.commit()

    return emprunt.id_emprunt


def read_emprunt(session, id_emprunt):
    
    return session.query(Emprunt).get(id_emprunt)


def retourner_livre(session, id_emprunt):
    
    emprunt = read_emprunt(session, id_emprunt)

    if emprunt and not emprunt.date_retour:
        # Enregistrer la date de retour
        emprunt.date_retour = date.today()

        # Augmenter le nombre d'exemplaires disponibles
        livre = read_livre(session, emprunt.isbn)
        if livre:
            livre.exemplaires_dispo += 1

        session.commit()
        return True

    return False


def delete_emprunt(session, id_emprunt):
    
    emprunt = read_emprunt(session, id_emprunt)

    if emprunt:
        session.delete(emprunt)
        session.commit()
        return True

    return False


# ============================================================
#                     FONCTIONS UTILES
# ============================================================

def get_all_etudiants(session):
    
    return session.query(Etudiant).order_by(Etudiant.nom, Etudiant.prenom).all()


def get_all_livres(session):
    
    return session.query(Livre).order_by(Livre.titre).all()


def get_emprunts_actifs(session):
    
    return session.query(Emprunt).filter(Emprunt.date_retour == None).all()
