

from typing import Dict, Optional
import os
from dotenv import load_dotenv
load_dotenv()


class Settings():
    VERSION: str = "1.0.0"
    PROJECT_NAME: str = "Fake News Detection API"
    debug: bool = True
    TWITTER_TOKEN = os.getenv("TWITTER_TOKEN")
    XAI_API_KEY = os.getenv("XAI_API_KEY")

settings = Settings()
