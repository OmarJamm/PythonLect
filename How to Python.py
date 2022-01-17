print("Hello Python")

name = "Omar"
surname = "Jammoul"
print(name + " " + surname)

user_input = input("Please enter your course name: ")
print(type(user_input))
print("The user entered", user_input)

age = int(input("Please enter your age: "))   # type cast string to int
print(type(age))
print("The user's age is ", age)

str_age = str(age)
print(type(str_age))                           # type cast int to string

gpa = float(input("Please enter your gpa: "))   # type cast string to float
print(type(gpa))
print("Ther student's gpa is ", gpa)