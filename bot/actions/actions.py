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

def get_info(all_data, info):
    list = ''
    for data in all_data:
       list += data[info] 
       list += '\n'
    return list

#-------------------------------------------

class ActionInsurers(Action):
   def name(self):
      return "insurers"

   def run(self, dispatcher, tracker, domain):
      response = get_data('insurer')
      print(response)
      dispatcher.utter_message('Ok, aqui está a sua lista de seguradoras:')
      info = get_info(response, 'site')
      dispatcher.utter_message(info)

class ActionCustomers(Action):
   def name(self):
      return "customers"

   def run(self, dispatcher, tracker, domain):
      response = get_data('customer')
      names = get_info(response, 'name')
      dispatcher.utter_message('Ok, aqui está a sua lista de clientes:')
      dispatcher.utter_message(names)
