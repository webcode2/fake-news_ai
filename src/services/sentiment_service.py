# services/sentiment_service.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

class SentimentService:
    def __init__(self):
        model_id = "cardiffnlp/twitter-roberta-base-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_id)
        self.pipeline = pipeline(
            "sentiment-analysis", 
            model=self.model, 
            tokenizer=self.tokenizer, 
            top_k=None
        )

    def analyze(self, text: str):
        return self.pipeline(text)
