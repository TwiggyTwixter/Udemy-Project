# Apply the try and except statements to the student grades program and keep it from crashing

data_valid = False

while data_valid == False:
        grade1 = (input("First Test: "))
        try:
            grade1 = float(grade1)
            if grade1 < 0 or grade1 > 10:
                print("Grade should be between 0 and 10")
                continue
            else:
                data_valid = True
        except:
            print("Invalid input")



data_valid = False

while data_valid == False:
        grade2 = (input("Second Test: "))
        try:
            grade2 = float(grade1)
            if grade2 < 0 or grade2 > 10:
                print("Grade should be between 0 and 10")
                continue
            else:
                data_valid = True
        except:
            print("Invalid input")

data_valid = False

while data_valid == False:
        total_classes = (input("Number of classes: "))
        try:
            total_classes = int(total_classes)
            if total_classes <= 0:
                print("The number of classes cannot be zero or less")
                continue
            else:
                data_valid = True
        except:
            print("Invalid input")



data_valid = False

while data_valid == False:
        absences = (input("Number of absences: "))
        try:
            absences = int(absences)
            if absences < 0 or absences > total_classes:
                print("The number of abscenses cannot be zless than zero or greater than the number of total classes")
                continue
            else:
                data_valid = True
        except:
            print("Invalid input")


avg_grade = ((grade1 + grade2)  / 2)
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance * 100),2))+ '%')

if(avg_grade >= 6 and attendance >= 0.8):
        print("The student has been approved.")
elif(avg_grade > 6 and attendance > 0.8):
        print("The student has failed due to an attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("The student has failed due to an average grade lower than 6.0")
else:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%.")