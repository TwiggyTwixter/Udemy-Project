# Store your age in a variable. then ask the user for his age and print whether:
# He's older than you.
#he's Younger than you.
# you have the same age

from doctest import master


print("Today I'll predict if you are younger than me, older than me, or if we're the same age.")
masterAge = 29
userAge = int(input("What is your age? "))

if(userAge > masterAge):
    print("You are ", userAge, " Which makes you older than me!")
elif (userAge < masterAge):
    print("You are ", userAge, " Which is younger than me!")
elif(userAge == masterAge):
    print("You are ", userAge, " Which is the same age as me!")