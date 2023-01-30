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
openai.api_key = environ["OPEN_KEY"]




def display_image_from_url(url):
    with urllib.request.urlopen(url) as url:
        image = plt.imread(url, format='jpg')
    plt.imshow(image)
    plt.tick_params(left=False,right=False,labelleft=False,labelbottom=False,bottom=False)
    plt.show()


 

# function  prints out the image url
def image(text_description):
    response = openai.Image.create(
        prompt = f"{text_description}",
        n=1,
        size="512x512"
    )
    return response["data"][0]["url"]
    
welcome = Figlet(font="slant")                                
print(welcome.renderText(text="AI Image Maker"))    
input("Press Enter/Return to continue.....")

run = True
while run:
    try:   
        
        image_description = input("Describe your image: ")                  
        image_url = image(image_description)                             
        print(                                              
            f'''
            The URL generated is: 

            {image_url}

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
            






