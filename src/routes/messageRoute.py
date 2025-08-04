import re
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from src.services.apiServices import convert_raw_sentiment_to_string
from src.controller import socialsController
from src.db.schemas.messageSchema import MessageRequest

router = APIRouter()


class SentimentRequest(BaseModel):
    text: str = ""
    model: str = None


# @router.post("/api/messages")
# async def analyze(query: str):
#     """ Analyze the sentiment of a given query.
#     """
#     if not query:
#         raise HTTPException(
#             status_code=400, detail="Query parameter is required")
#     result = await socialsController.analyze_sentiment(tweet=query)
#     if not result:
#         raise HTTPException(
#             status_code=500, detail="Failed to analyze sentiment")
#     return result


@router.post("/api/messages")
async def analyze1(request: Request, body: SentimentRequest):
    service = request.app.state.sentiment_service
    result = service.analyze(body.text)

    if body.model is None:
        if not result:
            raise HTTPException(
                status_code=500, detail="Failed to analyze sentiment")
        return {"sentiment": result}
    get_human_readable_sentiment = convert_raw_sentiment_to_string(
        asked_prompt=body.text, raw_sentiment=result,)
    return {"sentiment": get_human_readable_sentiment}
