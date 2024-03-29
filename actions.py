# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



class PickUpForm(FormAction):
    def name(self):
        return "pick_up_form"
    
    @staticmethod
    def required_slots(tracker):
        return[
            "address",
            "address2",
               ]
    def submit(
        self,
        dispatcher:CollectingDispatcher,
        tracker:Tracker,
        domain:Dict[Text,Any],
    )->List[Dict]:
        dispatcher.utter_message("Thank you for your information, we will inform of the pick up soon!")
        return[]
    
class InquireForm(FormAction):
    def name(self):
        return "inquire_form"
    @staticmethod
    def required_slots(tracker):
        return[
            "tracking_id",
        ]
    def submit(
        self,
        dispatcher:CollectingDispatcher,
        tracker:Tracker,
        domain:Dict[Text,Any],
    ) -> List[Dict]:
        #Need to get ETA , compute it using the map API
        dispatcher.utter_message("Your Package in currently being delivered. It is to be delivered at ETA 2.00pm today")
        return[]
        