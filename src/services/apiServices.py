import json
import os
import requests
from typing import Dict, Optional

from src.config.setting import settings


def convert_raw_sentiment_to_string(raw_sentiment: Dict, asked_prompt: str = "") -> Optional[str]:
    """
    Converts raw sentiment output into a human-readable explanation using the x.ai API.

    Args:
        raw_sentiment (Dict): Output from a sentiment analysis pipeline.
        asked_prompt (str): Original question or user input for context.

    Returns:
        str | None: Human-readable interpretation or None on failure.
    """

    api_key = settings.XAI_API_KEY

    if not api_key:
        print("❌ Error: XAI_API_KEY environment variable not set.")
        return None

    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

#     prompt = f"""
# Analyze this sentiment output: {raw_sentiment}
# Context: "{asked_prompt}"

# Instructions:
# - Classify sentiment as Positive, Neutral, or Negative.
# - Give score breakdown as percentages.
# - Summarize the most likely sentiment in 1–2 lines.
# - State if the input might spread misinformation or be harmful (Yes/No + reason).

# Be concise and factual. Avoid emotional or verbose language.
# """

#     prompt = f"""
# Analyze the following sentiment output: {raw_sentiment}
# Context: "{asked_prompt}"

# Instructions:
# 1. Classify the sentiment as **Positive**, **Neutral**, or **Negative**.
# 2. Provide a **score breakdown** (percentage for each class).
# 3. Summarize the most likely sentiment in 1-2 sentences.
# 4. Assess whether the input might contain **misinformation or be harmful** (respond with Yes/No and a brief reason).
# 5. Estimate a **truth_likelihood** score: High, Medium, or Low.
# 6. Set **flagged**: true if the input is misleading, dangerous, or needs moderation; otherwise, false.

# Respond using a structured, machine-readable markdown block with short, direct answers.
# Avoid emotional or verbose language.
# """

    prompt = f"""
Analyze the sentiment output: {raw_sentiment}
Context: "{asked_prompt}"

You are an AI assistant for a fake news detection platform.

Return a JSON object with the following fields:


    "overall_sentiment": "Positive | Neutral | Negative",
    "score_breakdown":dict[str, float] =>"LABEL_0-2 "
    "summary": "Short neutral summary of what the sentiment suggests and why.",
    "misinformation_or_harmful": "Yes | No",
    "reason": "Short explanation of the above answer.",
    "truth_likelihood": "High | Medium | Low",
    "flagged": true | false
  """

    payload = {
        "model": "grok-4",
        "stream": False,
        "temperature": 0.7,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        # Assuming x.ai returns a list of choices like OpenAI-style APIs

        # convert this json to dict

        print(result["choices"][0]["message"]["content"])

        print(raw_sentiment)
# convert the raw sentiment to percentage

        return {"data": result["choices"][0]["message"]["content"], }

    except requests.exceptions.RequestException as e:
        print(f"❌ HTTP Error: {e}")
    except KeyError:
        print(f"❌ Unexpected response structure: {response.text}")

    return None
