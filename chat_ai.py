import json
from wit import Wit
from translate import Translator
from PyDictionary import PyDictionary

access_token = "AOOEJH2MHT3YNXUTWBWTB2KYRAYBRLHI"
client = Wit(access_token= access_token)

dictionary = PyDictionary()
translator = Translator(to_lang="th")

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None
    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except Exception as e:
        pass
    return (entity,value)
def translate(message_text):
    mean = []

    meaning_JSON =  dictionary.meaning(message_text)
    meaning = json.loads(json.dumps(meaning_JSON))
    for key,values in meaning.items():
        temp = key+" : "
        for value in values:
            temp= temp + value +","
        mean.append(temp)
    tranlate = translator.translate(message_text)
    return mean,tranlate

