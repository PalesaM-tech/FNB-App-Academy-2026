#collect learner's name and marks for 3 subjects
#-----------METHOD 1----------------------
name = input("Enter the learners name: ")
mathematics = float(input("Enter the mathematics mark here: "))
chemistry = float(input("Enter the chemistry mark here: "))
accounting = float(input("Enter the accounting mark here: "))

subjects = [mathematics, chemistry, accounting] #use for loop (subject with <40 need intervention)


student = {"name": name,
           "Mathematics": mathematics,
           "Chemistry": chemistry,
           "Accounting": accounting}

#calculate the average
total = student["Mathematics"] + student["Chemistry"] + student["Accounting"]
average = round(total / 3, 2)
#---method 2--- average = (mathematics + chemistry + accounting) / 3

#print(average)
print(f"Hello {student['name']}, your average for the semester is: {average}")

if average >=80:
    print("Your grade is A(80+)")
elif average >= 70:
    print("Your grade is B(70-79)")
elif average >= 60:
    print("Your Grade is C(60-69)")
elif average >=50:
    print("Your Grade is D(50-59)")
else:
    print("Your grade is F(below 50)")

if average >=50:
    print("Congratulations, you have passed.")
else:
    print("Unfortunately, you have failed.")

#REMEMBER TO GOT THROUGH FOR LOOPS FOR THIS
if mathematics <40:
    print("Mathematics needs intervention.")

if chemistry <40:
    print("Chemistry needs intervention.")

if accounting <40:
    print("Accounting needs intervention.")

#-------------method 2---------------------------
#student1 = {"name": input("Enter your name: "),
           #"Mathematics": float(input("Enter the mark here: ")),
           #"Chemistry": float(input("Enter the mark here: ")),
           #"Accounting": float(input("Enter the mark here: "))}

print(student)
#print(student)
#calculate the average



#print(average)
#assign a grade and a status
#display full report cards
#for value  in enumerate (student, start=1):
   # print(value)