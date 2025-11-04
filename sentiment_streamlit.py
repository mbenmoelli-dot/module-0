import streamlit as st
import requests
from loguru import logger

# Configuration du logging
logger.add("logs/sentiment_streamlit.log", rotation="500 MB", level="INFO")

API_URL = "http://127.0.0.1:9000/analyse_sentiment/"

st.title("Analyse de Sentiment (VADER)")

texte = st.text_area("Entrez un texte en anglais :", height=150)

if st.button("Analyser"):
    if texte.strip() != "":
        logger.info(f"Texte soumis : {texte}")
        try:
            response = requests.post(API_URL, json={"texte": texte})
            response.raise_for_status()  # si erreur HTTP, exception levée

            sentiment = response.json()

            st.subheader("Résultats :")
            st.write(f"Polarité négative : {sentiment['neg']}")
            st.write(f"Polarité neutre : {sentiment['neu']}")
            st.write(f"Polarité positive : {sentiment['pos']}")
            st.write(f"Score composé : {sentiment['compound']}")

            # Interprétation du score composé
            if sentiment['compound'] >= 0.05:
                st.success("Sentiment global : Positif 😀")
            elif sentiment['compound'] <= -0.05:
                st.error("Sentiment global : Négatif 🙁")
            else:
                st.info("Sentiment global : Neutre 😐")

            logger.info(f"Résultat affiché : {sentiment}")

        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion à l'API : {e}")
            logger.error(f"Erreur API : {e}")

        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
            logger.error(f"Erreur générale : {e}")
    else:
        st.warning("Veuillez entrer du texte pour l'analyse.")