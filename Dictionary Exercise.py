#create a program with a predefined dictionary for a person. Include the folloowing infromatino: name, gender, age, address and phone.
#Ask the user what information he wants to know about the person, then print the value associated to that key or display a message in case the key is not found.

person = {"name": "Jazz", "gender": "male", "age": 29, "address": "USA", "phone": "123-456-7890"}

userInput = input("What property of this user do you seek? ")

print(person.get(userInput.lower(), "I'm sorry this information is unavailable."))