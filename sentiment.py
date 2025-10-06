# sentiment.py
from textblob import TextBlob

def analyze_sentiment(text: str) -> float:
    """
    Returns polarity score between -1.0 (negative) and +1.0 (positive).
    """
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity
    except Exception:
        # fallback in case TextBlob fails
        negative_words = ["sad", "depressed", "suicide", "hurt", "lonely", "anxious", "angry"]
        score = 0.0
        text_lower = text.lower()
        for w in negative_words:
            if w in text_lower:
                score -= 0.5
        return max(-1.0, min(1.0, score))
