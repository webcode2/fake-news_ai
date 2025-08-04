from fastapi import HTTPException
from src.services.apiServices import convert_raw_sentiment_to_string

# # social.py
# from pathlib import Path
# import json

# from src.config.tweepy import search_tweets


async def analyze_sentiment(tweet: str = "Elon Musk is Death"):
    """
    Analyze the sentiment of a given tweet.
    """
    try:
        # Run sentiment analysis
        result = sentiment_pipeline(tweet)
        data = convert_raw_sentiment_to_string(
            asked_prompt=tweet, raw_sentiment=result)
        if not data:
            raise HTTPException(
                status_code=500, detail="Failed to convert sentiment to string")
        # Return the sentiment result
        return data
    except Exception as e:
        print(f"❌ Error analyzing sentiment: {e}")
        raise HTTPException(status_code=500, detail=str(e))
