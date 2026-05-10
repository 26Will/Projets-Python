# Projet de Traitement de Données Cinématographiques - Groupe 15B

## 📝 Description
Ce projet a été réalisé dans le cadre d'une SAE (Situation d'Apprentissage et d'Évaluation). Il consiste en un script Python permettant d'automatiser l'extraction, le nettoyage et l'analyse de données provenant d'une base de données brute de films.

Le script transforme un fichier texte non structuré en un fichier **CSV propre et standardisé**, tout en générant un rapport statistique complet sur la collection de films traitée.

## 🚀 Fonctionnalités
- **Extraction de données** : Analyse un fichier source `.txt` complexe (séparateurs spécifiques `title=`, `type=`, etc.).
- **Nettoyage automatique** : 
  - Normalisation des titres (Majuscule au début).
  - Gestion des données manquantes (remplacement par `"N/A"`).
  - Nettoyage des descriptions (suppression des guillemets conflictuels).
- **Formatage CSV "GitHub-Ready"** : Utilisation de l'encodage **UTF-8**, de délimiteurs virgules et de guillemets pour assurer un affichage parfait sous forme de tableau sur GitHub.
- **Analyse Statistique** : Génération d'un fichier de résumé incluant :
  - Nombre total de films.
  - Scores (minimum, maximum, moyenne).
  - Répartition par genre (Taux de films d'action et de drames).

## 📁 Structure du Projet
Le projet est organisé de la manière suivante :
```text
.
├── data_base/          # Dossier contenant les fichiers bruts (.txt)
├── data_res/           # Dossier de sortie (fichiers .csv et rapports générés)
└── prog/               # Dossier contenant le script Python principal

⚙️ Installation et Utilisation
Clonez ce dépôt.

Placez votre fichier source groupe15B_data.txt dans le dossier data_base.

Lancez le script depuis le dossier prog :
"sae prog.py"

Retrouvez les résultats dans le dossier data_res.

🛠️ Détails Techniques
Encodage et Compatibilité
Le script utilise l'encodage UTF-8 pour garantir la portabilité des caractères accentués français sur tous les systèmes d'exploitation et sur GitHub.

Note pour l'ouverture sous Excel
Le fichier CSV généré utilise la virgule comme séparateur (standard international). Pour l'ouvrir correctement dans Excel (version française) :

Ouvrez Excel.

Allez dans l'onglet Données > À partir d'un fichier texte/CSV.

Sélectionnez le fichier et choisissez Virgule comme délimiteur dans l'aperçu.

👨‍💻 Auteur
William Houblon-Tchagam
