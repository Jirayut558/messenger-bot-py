import urllib
import urllib2
from bs4 import BeautifulSoup
from chat_ai import translate_response

def translate_fucntion(messaging_text):
    word = messaging_text.lower().replace("translate.", "").replace("tr.", "").strip()
    word, tran, meaning = translate_response(word)
    messaging_text = word + " : " + tran + "\n" + meaning
    return messaging_text
def youtube_function(text):
    word = text.lower().replace("youtube.", "").replace("y.", "").strip()
    textToSearch = word
    query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    link=""
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if link == "":
            link =  'https://www.youtube.com' + vid['href']
    return link