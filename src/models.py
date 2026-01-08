# ============ ORM SQLAlchemy ============

from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import date

# Base pour tous nos modèles
Base = declarative_base()


# ============ MODÈLE ÉTUDIANT ============
class Etudiant(Base):
    __tablename__ = 'etudiant'

    # Les colonnes de la table
    id_etud = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    date_inscription = Column(Date, default=date.today)
    solde_amende = Column(Numeric(5, 2), default=0)

    # Relation avec les emprunts (un étudiant peut avoir plusieurs emprunts)
    emprunts = relationship("Emprunt", back_populates="etudiant")

    def __repr__(self):
        return f"<Etudiant: {self.nom} {self.prenom}>"


# ============ MODÈLE LIVRE ============
class Livre(Base):
    __tablename__ = 'livre'

    # Les colonnes
    isbn = Column(String(13), primary_key=True)
    titre = Column(String(200), nullable=False)
    editeur = Column(String(100))
    annee = Column(Integer)
    exemplaires_dispo = Column(Integer, default=1)

    # Relation avec les emprunts
    emprunts = relationship("Emprunt", back_populates="livre")

    def __repr__(self):
        return f"<Livre: {self.titre}>"


# ============ MODÈLE EMPRUNT ============
class Emprunt(Base):
    __tablename__ = 'emprunt'

    # Les colonnes
    id_emprunt = Column(Integer, primary_key=True, autoincrement=True)
    id_etud = Column(Integer, ForeignKey('etudiant.id_etud'), nullable=False)
    isbn = Column(String(13), ForeignKey('livre.isbn'), nullable=False)
    date_emprunt = Column(Date, nullable=False, default=date.today)
    date_retour = Column(Date)
    amende = Column(Numeric(5, 2), default=0)

    # Relations (pour facilement accéder à l'étudiant et au livre)
    etudiant = relationship("Etudiant", back_populates="emprunts")
    livre = relationship("Livre", back_populates="emprunts")

    def __repr__(self):
        return f"<Emprunt: {self.id_emprunt}>"
