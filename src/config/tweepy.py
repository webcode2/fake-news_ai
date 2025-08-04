import tweepy

def search_tweets(query: str, max_results: int = 100):
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    response = client.search_recent_tweets(query=query, max_results=max_results)
    return response.data
