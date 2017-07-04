import os,sys
import string

from flask import Flask,request
from pymessenger import Bot
from chat_ai import wit_response,translate_response

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAbJRj9soeIBAGYbUV19paK3GfceSMRmkWRW2rAyVZBHyOaREQTBHwhh33qx7RLwm0QfGwRruLrFxypEM7q81N6nQDHDZAWiP9sKhw5sPX5HGu2XUmEZBTEDfhUbZBRzyDrxT50pP9TUBW4AJLmQeK1ZCB8YwZAH3ViYpB3tTL4wZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/',methods = ['GET'])
def verify():
    #webhook verification
    if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="hello":
            return "Verification token mismatch",403
        return request.args["hub.challenge"],200
    return "Hello world",200

@app.route('/',methods = ['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:
				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					if "no text" not in messaging_text.lower():
						if "translate" in messaging_text.lower():
							word = messaging_text.lower().replace("translate","").strip()
							tran,meaning = translate_response(word)
							messaging_text = word+" : "+tran+"\n"+meaning
						response = messaging_text
					# Echo
					bot.send_text_message(sender_id, response)
	return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug  = True,port = 80)
