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
from rasa_sdk.events import SlotSet
import requests

class ChangeTimeForm(FormAction):
    def name(self):
        return "changeTime_form"
    @staticmethod
    def required_slots(tracker):
        return ["tracking_id","startTime","endTime"]
    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any],)->List[Dict]:
        trackingID=tracker.get_slot("tracking_id")
        startTime=tracker.get_slot("startTime")
        endTime=tracker.get_slot("endTime")
        data={"rowID":trackingID,"start":startTime,"end":endTime}
        r = requests.get("https://supple-folder-256709.appspot.com/changeTime",data)
        list = r.text.split(',')
        if(list[0]=='possible'):
            dataD = {"rowID":trackingID}
            d = requests.get("https://supple-folder-256709.appspot.com/confirmChangeTime",dataD)
            response = "Route updated. Please check your ETA in a while."
        else:
            response = "Sorry we are unable to meet your schedule. The parcel will be delivered tomorrow."
            
        dispatcher.utter_message(response)
        return [SlotSet("tracking_id",None)]
    

class InquireForm(FormAction):  
    def name(self):
        return "inquire_form"
    @staticmethod
    def required_slots(tracker):
        return[
            "tracking_id"
        ]
    def submit(
        self,
        dispatcher:CollectingDispatcher,
        tracker:Tracker,
        domain:Dict[Text,Any],
    ) -> List[Dict]:
        #Need to get ETA , compute it using the map API
        #Run JSON get request and parse the response
        trackingID = tracker.get_slot("tracking_id")
        data = {"rowID":trackingID}
        r = requests.get("https://supple-folder-256709.appspot.com/getEta",data)
        response = "Your ETA is "+ r.text
        dispatcher.utter_message(response)
        return [SlotSet("tracking_id", None)]
        