import os,sys
import json
from flask import Flask,request
from pymessenger import Bot
import requests
import sheet

command_word = ['translate.','tr.']

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
					#----- Extracting text message -----
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'
					#----- Function Command -----
					if "no text" not in messaging_text.lower():
						res = bot_response(messaging_text)
						sheet.write_sheet_data(messaging_text)
						bot.send_text_message(sender_id, res)
	return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

def bot_response(inputtext):
	url = 'http://ping.aiya.ai:5004/chat?m='+inputtext
	response = requests.get(url)
	return response.text
if __name__ == '__main__':
    app.run(debug  = True,port = 80)
