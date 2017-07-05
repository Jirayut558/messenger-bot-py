import json
import re
import autocomplete

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
def translate_response(message_text):
    try:
        meaning_JSON =  dictionary.meaning(message_text)
        meaning = json.loads(json.dumps(meaning_JSON))
        tran = translator.translate(message_text)
        if 'none' not in str(meaning).lower():
            mean = ''
            for key,values in meaning.items():
                mean = mean + key+" : "+values[0]+"\n"
            return message_text,tran,mean
        else:
            isvalid = False
            isvalid,pre_word = autocomplete_word(message_text)
            if isvalid:
                meaning_JSON = dictionary.meaning(pre_word)
                meaning = json.loads(json.dumps(meaning_JSON))
                tran = translator.translate(pre_word)
                if 'none' not in str(meaning).lower():
                    mean = ''
                    for key, values in meaning.items():
                        mean = mean + key + " : " + values[0] + "\n"
                    return pre_word, tran, mean
                else:
                    return pre_word, tran, ""
            else:
                return message_text,pre_word,""
    except:
        return "","",""
def autocomplete_word(text):
    try:
        autocomplete.load()
        autoword = autocomplete.predict_currword(text)
        autoword = re.sub(r'[^\w]', ' ', str(autoword[0]))
        autoword = re.sub(r'\d+', ' ', autoword)
        return True,autoword.strip()
    except:
        return False,"Can not predict word"
''''def main():
if __name__ == '__main__':
    main()'''
