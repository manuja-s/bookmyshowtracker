import requests
import time
import webbrowser
import winsound
import keyboard
import datetime
from bs4 import BeautifulSoup
import pyttsx3
check_date = "20211227" #date in string format YMD EG: 12-01-2019 will look like 20190112
engine = pyttsx3.init()
URL = "https://in.bookmyshow.com/buytickets/spider-man-no-way-home-kochi/movie-koch-ET00319539-MT/"+check_date #pass the url for movie from bookmyshow website

def repeatedfun():
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    table = soup.find_all('a', attrs = {'class':'__venue-name'})
    for tag in table:
        date_url = tag['href']
        print(date_url)
        stripped_tag = tag.text.strip()
        print("20211227" in date_url)
        if (check_date in date_url):
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            engine.say("Booking open. Press Q to open book my show")
            print("Press Q to open bookmyshow")
            engine.runAndWait()

def background(): #infinte looping function for continues check
    while True:
        time.sleep(3)
        print(datetime.datetime.now())
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            webbrowser.open(
                'https://in.bookmyshow.com/buytickets/spider-man-no-way-home-kochi/movie-koch-ET00319539-MT/'+check_date,
                new=2)
            print('You Pressed Q!')
            break  # finishing the loop
        else:
            pass
        repeatedfun()


background()
