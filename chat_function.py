import urllib.parse
import urllib.request
#import urllib
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
    #query = urllib.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    #response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)

    elements = []
    i = 0
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if i <= 5:
            link =  'https://www.youtube.com' + vid['href']
            element = {
                'title': vid['title'],
                'buttons': [{
                    'type': 'web_url',
                    'title': "View",
                    'url': link,
                    "webview_height_ratio": "full"
                            }],
            }
            elements.append(element)
            i+=1

    return elements
'''def main():
    print youtube_function("Hello")
if __name__ == '__main__':
    main()'''