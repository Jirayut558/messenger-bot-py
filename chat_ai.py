from wit import Wit
access_token = "AOOEJH2MHT3YNXUTWBWTB2KYRAYBRLHI"
client = Wit(access_token= access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None
    print resp
    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except Exception as e:
        pass
    return (entity,value)

