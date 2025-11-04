from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger
from nltk.sentiment import SentimentIntensityAnalyzer

# Configuration du logging
logger.add("logs/sentiment_api.log", rotation="500 MB", level="INFO")

app = FastAPI(title="API Analyse de Sentiment VADER")

# Modèle de données reçu par la requête
class Texte(BaseModel):
    texte: str

# Initialiser l'analyseur de sentiments
sia = SentimentIntensityAnalyzer()

@app.post("/analyse_sentiment/")
async def analyse_sentiment(texte_object: Texte):
    logger.info(f"Texte reçu : {texte_object.texte}")
    try:
        # Analyse du texte
        sentiment = sia.polarity_scores(texte_object.texte)
        logger.info(f"Résultats : {sentiment}")

        # Retour des scores
        return {
            "neg": sentiment["neg"],
            "neu": sentiment["neu"],
            "pos": sentiment["pos"],
            "compound": sentiment["compound"]
        }

    except Exception as e:
        logger.error(f"Erreur : {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de l'analyse du texte")