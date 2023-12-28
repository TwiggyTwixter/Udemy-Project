#Create a program that asks the user for his birthday in the format "DD-MM-YYYY" Then Print: You were born in [month]
print("Today I will be guessing which month you were born in.")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemember", "December")
dob = input("Please enter your date of birth in the following format: DD-MM-YYYY: ")

dobMonth = int(dob[3:5]) - 1
print("Your Date of Birth Month is: ", months[dobMonth])


#Create a program with a predefined list of people. Ask the user for his name, add it to the end of the list and print the updated list.
students = ["Jordan", "Douglas", "Kandace", "Skip"]
newStudent = input("Welcome to registeration. Please add your name to our list: ")
students.append(newStudent)
print("You have been successfully added to the class. Here is the roster: ", students)
