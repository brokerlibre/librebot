from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests

#-------------------------------------------

def get_data(complement=''):
    response = 'Connection problem :/'
    try:
        response = requests.get('https://libreapi.temposerver.ml/api/{}'.format(complement))
    except ValueError:
        print(ValueError)
    return response.json()

def get_names(all_data):
    list = ''
    for data in all_data:
       list += data['name'] 
       list += '\n'
    return list

#-------------------------------------------

class ActionTest(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
      response = get_data('customer')
      names = get_names(response)
      dispatcher.utter_message(names)
