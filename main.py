from dotenv import load_dotenv
from os import environ
import openai
from requests import request
from json import loads
from random import randint



load_dotenv(".env")
NEWS_KEY = environ["NEWS_KEY"]
NEWS_ENDPOINT = environ["NEWS_ENDPOINT"]
openai.api_key = environ["OPEN_KEY"]

# function to get the news headline from newspi.org
def create_headline():
    random_index = randint(0, 25)
    response = request("GET", f"{NEWS_ENDPOINT}{NEWS_KEY}")
    formatted = response.text
    parse_json = loads(formatted)
    news_title = parse_json["articles"][random_index]["title"]
    return news_title
 

# function that takes in the headline and prints out the image url
def image(headline):
    response = openai.Image.create(
        prompt = headline,
        n=1,
        size="512x512"
    )
    print(response["data"][0]["url"])
    
# Store the headline in new_headline 
# Convert to String and pass to the image function
# image function will print to the console the created link 
new_headline = create_headline()

try:
    image(str(new_headline))
except Exception as e:
    print(e)





