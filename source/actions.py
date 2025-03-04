# This files contains your custom source which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from know_base import search_knowledge_base

class ActionSearchKnowledgeBase(Action):
    def name(self):
        return "action_search_knowledge_base"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        question = tracker.get_slot("question") or tracker.latest_message.get("text")
        result = search_knowledge_base(question)
        if result:
            dispatcher.utter_message(text=result[:500])  # Limit response length
        else:
            dispatcher.utter_message(response="utter_fallback")
        return []

class ActionRequestHuman(Action):
    def name(self):
        return "action_request_human"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        dispatcher.utter_message(text="I'll connect you to a human agent soon.")
        # Placeholder: Integrate with a messaging system or CRM to notify a human
        return []