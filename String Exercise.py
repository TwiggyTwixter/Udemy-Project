# String excercise

# Create a program that asks the user for his first, middle and last name, then print: "Your initials are ___"



firstName = (input("Please enter your first name: "))
middleName = (input("Please enter your middle name: " ))
lastName = (input("Please enter your middle name: "))

print("Your initials are: ",firstName[0],middleName[0],lastName[0])



#Company has a product with this lot number: "307-00901-00027" 037 is counrtry code, 00901 is product code and 00027 is the batch number
# create a program to print:
# Country Code: ___
# Product code: _____
# Batch number: _____


lotNumber = "307-00901-00027"
print("Country Code:", lotNumber[:3])
print("Product Code:", lotNumber[4:9])
print("Batch Number:", lotNumber[10:])