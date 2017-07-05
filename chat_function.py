import urllib.parse
import urllib.request
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
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    link=""
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if link == "":
            link =  'https://www.youtube.com' + vid['href']
    return link
'''def main():
    print youtube_function("Hello")
if __name__ == '__main__':
    main()'''