from dotenv import load_dotenv
from os import environ
import openai
from requests import request
from json import loads
from random import randint
from pyfiglet import Figlet
import matplotlib.pyplot as plt
import urllib.request


load_dotenv(".env")
NEWS_KEY = environ["NEWS_KEY"]
NEWS_ENDPOINT = environ["NEWS_ENDPOINT"]
openai.api_key = environ["OPEN_KEY"]




def display_image_from_url(url):
    with urllib.request.urlopen(url) as url:
        image = plt.imread(url, format='jpg')
    plt.imshow(image)
    plt.tick_params(left=False,right=False,labelleft=False,labelbottom=False,bottom=False)
    plt.show()


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
    return response["data"][0]["url"]
    
welcome = Figlet(font="slant")                                           # New Figlet for asccii text
print(welcome.renderText(text="News Headline Image Maker....."))         # Print the text out
input("Press Enter/Return to continue.....")

run = True
while run:
    try:                                                                     # Try block to catch exceptions
        new_headline = create_headline()                                     # saving the new headline
        image_url = image(str(new_headline))                                 # converting the headline to a string for the image function
        print(                                                               # print out the headline 
            f'''
            The URL generated is: 

            {image_url}

            This is the headline the image was generated from:

            {new_headline}
            '''
            )     
        display_image_from_url(image_url)
        keep_running = input("Try Again (y/n)?: ")                          
        if keep_running != "y":
            run = False
    except Exception as e:
        print(f"Oops something went wrong: {e}")
        keep_running = input("Try Again (y/n)?: ")
        if keep_running != "y":
            run = False
            






