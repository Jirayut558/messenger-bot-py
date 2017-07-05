from chat_ai import translate_response

def translate_fucntion(messaging_text):
    word = messaging_text.lower().replace("translate.", "").replace("tr.", "").strip()
    word, tran, meaning = translate_response(word)
    messaging_text = word + " : " + tran + "\n" + meaning
    return messaging_text
