# Create a program that asks the user for 8 names of people and store them in a list. When all the names have been give, picka random one and print it
# My solution
import random
x = 1
people = []

print("I need help with a project. Make a list of 8 people and I'll randomly pick one")

while x < 9:
    person = input("person " + str(x) + ": ")
    people.append(person)
    x += 1

randonumber = random.randint(0,7)
print("Alright I choose", people[randonumber])

#-----------------------------------------------
#Udemy Solution
people = []

for x in range(0,8):
    person = input("Type the name of a person: ")
    people.append(person)

index = random.randint(0,7)

random_person = people[index]
print("Picking a random person: ", random_person)
