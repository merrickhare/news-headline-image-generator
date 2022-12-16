from dotenv import load_dotenv
from os import environ
import openai
from requests import request
import json
import random

load_dotenv(".env")
NEWS_KEY = environ["NEWS_KEY"]
NEWS_ENDPOINT = environ["NEWS_ENDPOINT"]
openai.api_key = environ["OPEN_KEY"]


def create_headline():
    random_index = random.randint(0, 25)
    try:
        response = request("GET", f"{NEWS_ENDPOINT}{NEWS_KEY}")
        formatted = response.text
        parse_json = json.loads(formatted)
        news_title = parse_json["articles"][random_index]["title"]
        news_article = parse_json["articles"][random_index]["content"]
        return news_title, news_article
    except Exception as e:
        return e

def image(headline):
    response = openai.Image.create(
        prompt = headline,
        n=1,
        size="512x512"
    )
    print(response["data"][0]["url"])

def create_summary(article):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f"Summarize this for a ninth-grade student:{article}",
        max_tokens = 4,
        temperature = 0
    )
    return response



new_headline = create_headline()
image(str(new_headline[0]))

