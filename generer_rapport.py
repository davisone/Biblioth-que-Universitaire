"""
Script de génération de rapport PDF pour le projet Bibliothèque Universitaire
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from datetime import datetime


def generer_rapport_pdf():
    """Génère un rapport PDF complet du projet"""

    # Configuration du document
    nom_fichier = "Rapport_Projet_Bibliotheque.pdf"
    doc = SimpleDocTemplate(
        nom_fichier,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # Conteneur pour les éléments du PDF
    elements = []

    # Styles
    styles = getSampleStyleSheet()

    # Style personnalisé pour le titre
    style_titre = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Style pour les sous-titres
    style_sous_titre = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2563EB'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    # Style pour le texte normal
    style_normal = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )

    # Style pour le code
    style_code = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        leftIndent=20,
        rightIndent=20,
        textColor=colors.HexColor('#1F2937'),
        backColor=colors.HexColor('#F3F4F6'),
        spaceAfter=12
    )

    # ==================== PAGE DE TITRE ====================
    elements.append(Spacer(1, 3*cm))

    titre = Paragraph("Système de Gestion<br/>de Bibliothèque Universitaire", style_titre)
    elements.append(titre)

    elements.append(Spacer(1, 1*cm))

    sous_titre = Paragraph("Projet B3 Développement", style_sous_titre)
    elements.append(sous_titre)

    elements.append(Spacer(1, 2*cm))

    info_projet = f"""
    <para align=center>
    <b>Technologies utilisées :</b><br/>
    Python • Streamlit • PostgreSQL • SQLAlchemy<br/><br/>
    <b>Date du rapport :</b> {datetime.now().strftime('%d/%m/%Y')}<br/>
    </para>
    """
    elements.append(Paragraph(info_projet, style_normal))

    elements.append(PageBreak())

    # ==================== INTRODUCTION ====================
    elements.append(Paragraph("1. Introduction", style_sous_titre))

    intro_text = """
    Ce projet consiste en un système complet de gestion de bibliothèque universitaire
    développé en Python. L'application permet de gérer efficacement les livres, les
    étudiants, les emprunts et les amendes à travers une interface web intuitive
    construite avec Streamlit.
    """
    elements.append(Paragraph(intro_text, style_normal))
    elements.append(Spacer(1, 0.5*cm))

    # ==================== OBJECTIFS ====================
    elements.append(Paragraph("2. Objectifs du projet", style_sous_titre))

    objectifs = """
    • <b>Centraliser la gestion</b> : Regrouper toutes les opérations de la bibliothèque en un seul système<br/>
    • <b>Faciliter les emprunts</b> : Permettre un suivi en temps réel des livres empruntés<br/>
    • <b>Automatiser les amendes</b> : Calculer automatiquement les pénalités de retard<br/>
    • <b>Fournir des statistiques</b> : Offrir une vue d'ensemble via le tableau de bord<br/>
    """
    elements.append(Paragraph(objectifs, style_normal))
    elements.append(Spacer(1, 0.5*cm))

    # ==================== ARCHITECTURE ====================
    elements.append(Paragraph("3. Architecture technique", style_sous_titre))

    archi_text = """
    L'application suit une architecture en couches séparant clairement les responsabilités :
    """
    elements.append(Paragraph(archi_text, style_normal))

    # Tableau de l'architecture
    data_archi = [
        ['Couche', 'Description', 'Fichiers'],
        ['Présentation', 'Interface utilisateur Streamlit', 'app.py, modules/*.py'],
        ['Modèles', 'Classes SQLAlchemy (ORM)', 'models.py'],
        ['Accès données', 'CRUD et requêtes SQL', 'crud_orm.py, utils.py'],
        ['Base de données', 'PostgreSQL', 'database.py']
    ]

    table_archi = Table(data_archi, colWidths=[3.5*cm, 6*cm, 5.5*cm])
    table_archi.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F3F4F6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')])
    ]))

    elements.append(table_archi)
    elements.append(Spacer(1, 0.5*cm))

    # ==================== FONCTIONNALITÉS ====================
    elements.append(Paragraph("4. Fonctionnalités principales", style_sous_titre))

    fonctionnalites = """
    <b>4.1 Page d'accueil</b><br/>
    Tableau de bord affichant les statistiques clés :<br/>
    • Nombre total de livres dans le catalogue<br/>
    • Nombre d'étudiants inscrits<br/>
    • Emprunts en cours<br/>
    • Montant total des amendes<br/><br/>

    <b>4.2 Gestion des livres</b><br/>
    • Affichage du catalogue complet avec ISBN, titre, éditeur, année et disponibilité<br/>
    • Filtrage des livres disponibles<br/>
    • Recherche et consultation des informations détaillées<br/><br/>

    <b>4.3 Gestion des étudiants</b><br/>
    • Liste complète des étudiants inscrits<br/>
    • Informations : ID, nom, prénom, email, date d'inscription, solde d'amende<br/>
    • Suivi du statut de chaque étudiant<br/><br/>

    <b>4.4 Gestion des emprunts</b><br/>
    • Liste des emprunts en cours et terminés<br/>
    • Traçabilité complète : dates d'emprunt et de retour<br/>
    • Calcul automatique des amendes en cas de retard<br/><br/>

    <b>4.5 Gestion des amendes</b><br/>
    • Vue détaillée des amendes par étudiant<br/>
    • Suivi des paiements et des soldes<br/>
    • Historique des pénalités<br/><br/>

    <b>4.6 Module CRUD</b><br/>
    • Opérations Create, Read, Update, Delete sur toutes les entités<br/>
    • Interface d'administration complète<br/>
    • Gestion avancée des données<br/>
    """
    elements.append(Paragraph(fonctionnalites, style_normal))

    elements.append(PageBreak())

    # ==================== BASE DE DONNÉES ====================
    elements.append(Paragraph("5. Modèle de base de données", style_sous_titre))

    bd_text = """
    La base de données PostgreSQL comprend trois tables principales reliées par des clés étrangères :
    """
    elements.append(Paragraph(bd_text, style_normal))
    elements.append(Spacer(1, 0.3*cm))

    # Table Étudiant
    elements.append(Paragraph("<b>5.1 Table ETUDIANT</b>", style_normal))
    data_etudiant = [
        ['Colonne', 'Type', 'Description'],
        ['id_etud', 'INTEGER (PK)', 'Identifiant unique auto-incrémenté'],
        ['nom', 'VARCHAR(50)', 'Nom de l\'étudiant'],
        ['prenom', 'VARCHAR(50)', 'Prénom de l\'étudiant'],
        ['email', 'VARCHAR(100)', 'Email (unique)'],
        ['date_inscription', 'DATE', 'Date d\'inscription'],
        ['solde_amende', 'NUMERIC(5,2)', 'Montant des amendes dues']
    ]

    table_etudiant = Table(data_etudiant, colWidths=[4*cm, 4*cm, 7*cm])
    table_etudiant.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#10B981')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F3F4F6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8)
    ]))
    elements.append(table_etudiant)
    elements.append(Spacer(1, 0.5*cm))

    # Table Livre
    elements.append(Paragraph("<b>5.2 Table LIVRE</b>", style_normal))
    data_livre = [
        ['Colonne', 'Type', 'Description'],
        ['isbn', 'VARCHAR(13) (PK)', 'Numéro ISBN unique du livre'],
        ['titre', 'VARCHAR(200)', 'Titre du livre'],
        ['editeur', 'VARCHAR(100)', 'Maison d\'édition'],
        ['annee', 'INTEGER', 'Année de publication'],
        ['exemplaires_dispo', 'INTEGER', 'Nombre d\'exemplaires disponibles']
    ]

    table_livre = Table(data_livre, colWidths=[4*cm, 4*cm, 7*cm])
    table_livre.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F59E0B')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F3F4F6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8)
    ]))
    elements.append(table_livre)
    elements.append(Spacer(1, 0.5*cm))

    # Table Emprunt
    elements.append(Paragraph("<b>5.3 Table EMPRUNT</b>", style_normal))
    data_emprunt = [
        ['Colonne', 'Type', 'Description'],
        ['id_emprunt', 'INTEGER (PK)', 'Identifiant unique de l\'emprunt'],
        ['id_etud', 'INTEGER (FK)', 'Référence à l\'étudiant'],
        ['isbn', 'VARCHAR(13) (FK)', 'Référence au livre'],
        ['date_emprunt', 'DATE', 'Date de l\'emprunt'],
        ['date_retour', 'DATE', 'Date de retour (NULL si en cours)'],
        ['amende', 'NUMERIC(5,2)', 'Montant de l\'amende']
    ]

    table_emprunt = Table(data_emprunt, colWidths=[4*cm, 4*cm, 7*cm])
    table_emprunt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B5CF6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F3F4F6')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8)
    ]))
    elements.append(table_emprunt)

    elements.append(PageBreak())

    # ==================== EXEMPLES DE CODE ====================
    elements.append(Paragraph("6. Exemples de code", style_sous_titre))

    elements.append(Paragraph("<b>6.1 Définition du modèle Étudiant (SQLAlchemy)</b>", style_normal))

    code_etudiant = """
<font face="Courier" size="8">
class Etudiant(Base):
    __tablename__ = 'etudiant'

    id_etud = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    date_inscription = Column(Date, default=date.today)
    solde_amende = Column(Numeric(5, 2), default=0)

    # Relation avec les emprunts
    emprunts = relationship("Emprunt", back_populates="etudiant")
</font>
    """
    elements.append(Paragraph(code_etudiant, style_code))
    elements.append(Spacer(1, 0.3*cm))

    elements.append(Paragraph("<b>6.2 Requête SQL pour afficher les livres disponibles</b>", style_normal))

    code_sql = """
<font face="Courier" size="8">
requete = \"\"\"
    SELECT isbn, titre, editeur, annee, exemplaires_dispo
    FROM livre
    WHERE exemplaires_dispo &gt; 0
    ORDER BY titre;
\"\"\"
resultat = executer_requete_sql(requete)
tableau_livres = convertir_en_tableau(
    resultat,
    ["ISBN", "Titre", "Éditeur", "Année", "Exemplaires disponibles"]
)
</font>
    """
    elements.append(Paragraph(code_sql, style_code))
    elements.append(Spacer(1, 0.3*cm))

    elements.append(Paragraph("<b>6.3 Structure de navigation Streamlit</b>", style_normal))

    code_navigation = """
<font face="Courier" size="8">
page_selectionnee = st.sidebar.radio(
    "Aller à :",
    [
        "🏠 Accueil",
        "📚 Livres",
        "👨‍🎓 Étudiants",
        "📖 Emprunts",
        "💰 Amendes",
        "⚙️ Gestion CRUD"
    ]
)

if page_selectionnee == "🏠 Accueil":
    accueil.afficher()
elif page_selectionnee == "📚 Livres":
    livres.afficher()
# ... autres pages
</font>
    """
    elements.append(Paragraph(code_navigation, style_code))

    elements.append(PageBreak())

    # ==================== EXEMPLES DE SORTIES ====================
    elements.append(Paragraph("7. Exemples de sorties", style_sous_titre))

    elements.append(Paragraph("<b>7.1 Affichage du catalogue de livres</b>", style_normal))

    sortie_livres = """
<font face="Courier" size="8" color="#1F2937">
Exemple de sortie pour la page Livres :

+---------------+--------------------------------+------------------+------+----------------------+
| ISBN          | Titre                          | Éditeur          | Année| Exemplaires dispo    |
+---------------+--------------------------------+------------------+------+----------------------+
| 9782070360024 | Le Petit Prince                | Gallimard        | 1943 | 3                    |
| 9782253004226 | 1984                           | Livre de Poche   | 1950 | 2                    |
| 9782253151623 | Les Misérables                 | Livre de Poche   | 1862 | 1                    |
| 9782070413119 | L'Étranger                     | Gallimard        | 1942 | 0                    |
+---------------+--------------------------------+------------------+------+----------------------+

✅ 4 livre(s) trouvé(s)
</font>
    """
    elements.append(Paragraph(sortie_livres, style_code))
    elements.append(Spacer(1, 0.5*cm))

    elements.append(Paragraph("<b>7.2 Liste des étudiants inscrits</b>", style_normal))

    sortie_etudiants = """
<font face="Courier" size="8" color="#1F2937">
Exemple de sortie pour la page Étudiants :

+--------+----------+-----------+---------------------------+------------------+--------------+
| ID     | Nom      | Prénom    | Email                     | Date inscription | Solde amende |
+--------+----------+-----------+---------------------------+------------------+--------------+
| 1      | Dupont   | Jean      | jean.dupont@univ.fr       | 2024-09-01       | 0.00 €       |
| 2      | Martin   | Sophie    | sophie.martin@univ.fr     | 2024-09-05       | 5.50 €       |
| 3      | Bernard  | Lucas     | lucas.bernard@univ.fr     | 2024-09-10       | 0.00 €       |
| 4      | Petit    | Emma      | emma.petit@univ.fr        | 2024-09-15       | 12.00 €      |
+--------+----------+-----------+---------------------------+------------------+--------------+

✅ 4 étudiant(s) inscrit(s)
</font>
    """
    elements.append(Paragraph(sortie_etudiants, style_code))
    elements.append(Spacer(1, 0.5*cm))

    elements.append(Paragraph("<b>7.3 Statistiques du tableau de bord</b>", style_normal))

    sortie_stats = """
<font face="Courier" size="8" color="#1F2937">
Exemple de sortie pour la page d'accueil (Dashboard) :

📊 STATISTIQUES DE LA BIBLIOTHÈQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Livres au catalogue     : 245
👨‍🎓 Étudiants inscrits     : 89
📖 Emprunts en cours       : 42
💰 Amendes totales         : 127.50 €
✅ Livres disponibles      : 203
⏰ Retours en retard       : 8

Dernière mise à jour : 08/01/2026 14:30
</font>
    """
    elements.append(Paragraph(sortie_stats, style_code))

    elements.append(PageBreak())

    # ==================== GUIDE D'UTILISATION ====================
    elements.append(Paragraph("8. Guide d'installation et d'utilisation", style_sous_titre))

    elements.append(Paragraph("<b>8.1 Installation</b>", style_normal))

    install_text = """
<font face="Courier" size="9">
# 1. Cloner le repository
git clone [url-du-projet]
cd TP_python

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\\Scripts\\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer PostgreSQL
# Créer une base de données nommée 'bibliotheque'
# Mettre à jour les paramètres de connexion dans database.py
</font>
    """
    elements.append(Paragraph(install_text, style_code))
    elements.append(Spacer(1, 0.3*cm))

    elements.append(Paragraph("<b>8.2 Lancement de l'application</b>", style_normal))

    launch_text = """
<font face="Courier" size="9">
# Depuis le répertoire racine du projet
streamlit run src/app.py

# L'application s'ouvre automatiquement dans le navigateur
# URL par défaut : http://localhost:8501
</font>
    """
    elements.append(Paragraph(launch_text, style_code))
    elements.append(Spacer(1, 0.3*cm))

    elements.append(Paragraph("<b>8.3 Utilisation</b>", style_normal))

    usage_text = """
    <b>Navigation :</b> Utilisez le menu latéral pour accéder aux différentes sections<br/><br/>

    <b>Consultation :</b> Les pages Livres, Étudiants, Emprunts et Amendes affichent
    les données sous forme de tableaux interactifs avec possibilité de tri et de filtre<br/><br/>

    <b>Gestion CRUD :</b> La page "Gestion CRUD" permet d'effectuer toutes les opérations
    d'administration : ajout, modification et suppression d'enregistrements<br/><br/>

    <b>Tableau de bord :</b> La page d'accueil fournit une vue d'ensemble en temps réel
    des statistiques importantes de la bibliothèque
    """
    elements.append(Paragraph(usage_text, style_normal))

    # ==================== CONCLUSION ====================
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph("9. Conclusion", style_sous_titre))

    conclusion_text = """
    Ce système de gestion de bibliothèque universitaire offre une solution complète et
    moderne pour gérer efficacement l'ensemble des opérations d'une bibliothèque.
    L'utilisation de technologies actuelles (Python, Streamlit, PostgreSQL, SQLAlchemy)
    garantit performance, maintenabilité et évolutivité du système.<br/><br/>

    L'interface intuitive permet une prise en main rapide par les utilisateurs, tandis que
    l'architecture modulaire facilite les futures évolutions et l'ajout de nouvelles
    fonctionnalités.
    """
    elements.append(Paragraph(conclusion_text, style_normal))

    # ==================== GÉNÉRATION DU PDF ====================
    doc.build(elements)
    print(f"✅ Rapport PDF généré avec succès : {nom_fichier}")
    return nom_fichier


if __name__ == "__main__":
    generer_rapport_pdf()
