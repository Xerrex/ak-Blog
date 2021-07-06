import json
import requests
from flask import current_app
from flask_babel import _


def translate(txt, src_lang, dest_lang):
    """Live translate text

    Args:
        txt (String): the text string to be translated
        src_lang (String): The source language of the text to translate
        dest_lang ([type]): Destination language of which to translate text
    """
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        #return _('Error: the translation service is not configured.')
        return _('E: Translation coming soon')

    # auth = {
    #     'Ocp-Apim-Subscription-Key': 'KEY',
    #     'Ocp-Apim-Subscription-Region': 'region'
    #     }

    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    url = f'https://api.microsofttranslator.com/v2/Ajax.svc'\
                     '/Translate?text={txt}&from={src_lang}&to={dest_lang}'
    
    r = requests.get(url,headers=auth)

    if r.status_code != 200:
        #return _('Error: the translation service failed.')
        return _('E: Working on your translation')
    return json.loads(r.content.decode('utf-8-sig'))