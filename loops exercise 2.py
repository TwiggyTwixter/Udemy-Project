# Create a guess game with the names of colors. At each round pick a random color from a list and let the user try to guess it. When he does it, ask if he wants to play again. Keep playing until the user types "no"
# My solution
import random

play = "yes"
colors = ["Red", "Green", "Blue", "Purple", "Pink", "Orange"]

randonumber = random.randint(0,5)
color_to_guess = colors[randonumber]
print("Let's play a game.")


while play == "yes":
    color = input("Guess the color I'm thinking of: ")
    if color == color_to_guess:
        print("Yes! The color I'm thinking of is", color_to_guess)
        continue_playing = input("Want to play again? ")
        if continue_playing == "no":
            play = "no"
    else:
        print("Nope! Try again")
print("Thanks for playing!")

#---------------------------------------------------------
#Udemy Solution
colors = ["Red", "Green", "Blue", "Purple", "Pink", "Orange"]

while True:
    color = colors[random.randint(0,len(colors) -1 )]
    guess = input("I'm thinking about a color, can you guess it: ")

    while True:
        if (color == guess.lower()):
            break
        else:
            guess - input("Nope! Try again: ")
    print("You guessed it! I was thinking about", color)

    play_again = input("Let's play again? Type 'no' to quit.")

    if play_again.lower() == 'no':
        break
print("Thanks for playing!")