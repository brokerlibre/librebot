from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionTest(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
      dispatcher.utter_message("This is a custom action test message")
