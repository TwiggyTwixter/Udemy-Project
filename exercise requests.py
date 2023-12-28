# Example stuff below

# import requests
# r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
# print(r.status_code)
# print(r.text)
# print(type(r.text))

# import json
# question = json.loads(r.text)
# print(question)
# print(type(question))

# import pprint
# pprint.pprint(question)
# print(question['results'][0]['category'])

# person = {"Name": "Jazz", "Age": 30}
# person_json = json.dumps(person)
# print(person_json)


# Excerise: Create a quizzing game. Make an HTTP request to the Open Trivia API at each round of the game to get a new question and present it to the user to answer. At the end of each round, ask the user if he wants to play again. Keep playing forever until the user types "quit".
# Tell the user if the answer is incorrect or correct and keep the user's score.

import time
import requests
import json
import pprint

questions_asked = 0
question_number = 0
incorrect = 0
correct = 0
continue_game = 'y'
def getQuestions():
    r = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean")
    return json.loads(r.text)


print("Welcome to this Trivia Game. Here we will ask you true/false statements")

while continue_game == "y":
    if(question_number == 0):
        questions = getQuestions()

    Newquestion = questions['results'][question_number]['question'] + " "
    user_answer = input(Newquestion.replace('&quot;', '"')).lower()

    if user_answer in ["true", "t", "yes", 'y']:
        user_answer = "True"
    elif user_answer in ["false", "f", "no", "n"]:
        user_answer = "False"
    
    if user_answer == questions['results'][question_number]['correct_answer']:
        print('correct')
        correct += 1
    else:
        print('incorrect')
        incorrect += 1
    time.sleep(2)
    question_number += 1
    if question_number == 5:
        continue_game = input("Continue Game? (Y/N) ")  

print("# of questions asked: ", question_number)
print("Correct Answers ", correct)
print("Incorrect Answers", incorrect)
print("Score: " + str(((correct/question_number)*100)) + "%")