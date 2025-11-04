Projet : Analyse de sentiment avec FastAPI et Streamlit
=======================================================

Description
-----------
Ce projet permet d'analyser le sentiment d'un texte (en anglais) à l'aide du modèle VADER de la bibliothèque NLTK.
L'application est composée de deux parties :
1) Une API FastAPI qui analyse le texte et retourne les scores de sentiment au format JSON.
2) Une interface utilisateur Streamlit qui permet à l'utilisateur de saisir un texte et d'afficher les résultats.

Scores retournés :
- neg : proportion négative (0 à 1)
- neu : proportion neutre (0 à 1)
- pos : proportion positive (0 à 1)
- compound : score global (-1 à +1)

Structure du projet
-------------------
.
├── .venv/                       # Environnement virtuel Python
├── logs/                        # Fichiers de logs
│   ├── sentiment_api.log
│   └── sentiment_streamlit.log
├── sentiment_api.py             # Code de l'API FastAPI
├── sentiment_streamlit.py       # Interface utilisateur Streamlit
├── requirements.txt             # Dépendances du projet
└── README.txt                   # Documentation du projet

Installation
------------
1) Créer un environnement virtuel :
   python -m venv .venv

2) Activer l'environnement :
   Windows :
      Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
      .venv\Scripts\activate

3) Installer les dépendances :
   pip install -r requirements.txt

4) Télécharger le lexique VADER :
   python -c "import nltk; nltk.download('vader_lexicon')"

Exécution du projet
-------------------

1) Lancer l'API FastAPI :
   uvicorn sentiment_api:app --reload --host 127.0.0.1 --port 9000

   Documentation disponible :
   http://127.0.0.1:9000/docs

2) Dans un autre terminal, lancer Streamlit :
   streamlit run sentiment_streamlit.py

Accès à l'application
---------------------
- API : http://127.0.0.1:9000/docs
- Interface Streamlit : http://localhost:8501

Fonctionnement
--------------
Entrer un texte dans l'interface Streamlit, cliquer sur "Analyser".
Les scores de sentiment et l'interprétation (positif / neutre / négatif) s'affichent.

Logs
----
Les actions et erreurs sont enregistrées dans le dossier "logs".

Technologies utilisées
----------------------
- Python
- FastAPI
- Streamlit
- NLTK (VADER)
- Loguru
- Requests
- Uvicorn

Auteur
------
Projet réalisé dans le cadre de la formation Python / Data / IA (OPCO Atlas)