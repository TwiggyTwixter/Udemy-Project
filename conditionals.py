data_valid = False

while data_valid == False:
        grade1 = float (input("First Test: "))
        if grade1 < 0 or grade1 > 10:
                print("Grade should be between 0 and 10")
                continue
        else:
                data_valid = True 

data_valid = False

while data_valid == False:
        grade2 = float (input("Second  Test: "))
        if grade2 < 0 or grade2 > 10:
                print("Grade should be between 0 and 10")
                continue
        else:
                data_valid = True

data_valid = False

while data_valid == False:
        total_classes = int(input("Number of classes: "))
        if total_classes <= 0:
                print("The number of classes cannot be zero or less")
                continue
        else:
                data_valid = True

data_valid = False

while data_valid == False:
        absences = int(input("Number of absences: "))
        if absences < 0 or absences > total_classes:
                print("The number of abscenses cannot be zless than zero or greater than the number of total classes")
                continue
        else:
                data_valid = True

                





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