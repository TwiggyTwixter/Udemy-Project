import requests
import json
import pprint

def getQuestions():
    r = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean")
    return json.loads(r.text)

print(getQuestions()['results'][0]['correct_answer'])