#dictionaries
student = {"name": "John",
           "age": "26",
           "courses": ["History", "Maths", "Physics", "CompSci", "Art"]}

#student["phone"] = "067 067 0674"
#student["name"] = "Lulu"
#student.update({"name": "Palesa",
                #"age": "22",
                #"phone": "067 092 6781"})

#del student["age"]
#age = student.pop("age")
#print(age)

print(len(student))  #number of keys
print(student.keys())   #prints all the keys of our dictionary
print(student.values())  #prints all the values
print(student.items())   #to print the keys and values

for key in student:
     print(key)

for value in student:
     print(value)

for key, value in student.items():
     print(key, value)

print(student)
#print(student["age"])
print(student.get("courses"))
print(student.get("phone"))

#Lists, Tuples, Sets--------YouTube------------
#Empty Lists
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = {} #this is right, this is a dictionary
empty_set = set()

#-----------YouTube Sets explaination---------------------
#values that are unorder and dont have duplicates, sets through away duplicates
#when you run a set, the order of the list/set will always change because sets dont care about the order of the lists
#sets also test if a value is in a set, this is called membership test
cs_courses = {"History", "Art", "Maths", "Physics", "CompSci", "Art"}
art_courses = {"History", "Maths", "Design", "Art"}
print(cs_courses)
print("Art" in cs_courses)
print(cs_courses.intersection(art_courses)) #shows mutual courses in both sets
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#-----------YouTube Tuples(immutable) explaination----------------
#use tuple when you want a list that cant be modified, modifying the list gives result error
tuple_1 = ("History", "Maths", "Physics", "CompSci", "Art")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#-----------YouTube Lists[mutable] explaination-----------------
courses = ["History", "Maths", "Physics", "CompSci", "Art"]
#courses.append("Art")
#courses.append = "Art"
#courses.append = ("Art")  Ask in the group for assistance with the 3

sorted_courses = sorted(courses)
print(sorted_courses)

for course in courses: #you dont have to alwaysdefault to using "item" you can use maybe course since this is related to courses
    print(course)  #print statement goes to a new line, each time it is executed

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = "- ".join(course)
print(course_str)

nums = [2, 8, 6, 5, 1]
#nums.sort(reverse=True)
#courses.sort(reverse=True) #sorts in alphabetical order, if we had numbers it would sort numerically
#courses.reverse()

courses_2 = ["Pricing", "Surveying"]
#courses.extend(courses_2)  #extends the existing list
#courses.insert(0, courses_2) #inserts the course_2 list inside the existng list

#popped = courses.pop(1) #it will always pop/remove the last value and the value which is the index stated in the parentheses
#courses.pop()  #removes last value in the list, also useful for using the list like a stack
#print(popped)

#courses.extend(courses_2)  #extends the existing list
#courses.insert(0, courses_2) #inserts the course_2 list inside the existng list

#applying the min, max, sum variables
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses)
print("History" in courses)
print("Pricing" in courses)

#to print of find the index of a value in a list
print(courses.index("Physics"))

#print(courses[:3])  #slicing
#print(courses[1:])
#print(len(courses))


#----------------FNB ACADEMY EXPLAINATION----------------------
#Basic if/else statement script

age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket? (yes/no)")

if age>= 18 and section_pass == "yes":
    print("You have access granted to the VIP section !!! ")
elif age >= 18:
    print("Access granted to the general section !!!")
else: 
    print("Access denied !!!")




#calling a method to a list
names = ["Mahau", "Muchis", "Naledi", "Rethabile"]
names.append("Palesa")

print(names)

#calling a method to a string, method below replace the original object
module = "Surveying"
#module.upper()
#module = module.upper()

#calling a method by printing it. keeps the original object and only changes in the print function
print(module.upper())
print(module.title())

#creating a different variable in order to STORE the new method called
uppercase_module = module.upper()

print(uppercase_module)