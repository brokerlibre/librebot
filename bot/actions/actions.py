from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionTest(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
      dispatcher.utter_message("Esta é uma mensagem customizada!")
