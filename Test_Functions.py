def main():
    greeting("Omar")
    give1 = to_add()
    give2 = to_add()
    sumX = calculate_Sum(give1, give2)
    print_output2(sumX)
    to_multi()
    For_User()
    print("Hasal Kheir")

def greeting(name):
    print("Welcome to Python", name)


def calculate_Sum(a, b):      # definition of the function
    return a + b

def hundred_multi(number):
    '''This function multiplies a number given by the user by a hundred
     and prints the result'''
    print("Your number multiplied by 100 is: ", int(number*100))

def For_User():
    age = int(input("Please enter your age: "))    # for user age
    print("You wish your age is:", age)

def print_output(val):
    print(val)

def print_output2(sumVal):
    print("The sum of your numbers is: ", sumVal)

def to_add():
    val1 = int(input("Give a number to add "))
    return val1

def to_multi():
    mult2 = int(input("Give a number to x100: "))    
    print("Your number multiplied by 100 is: ", mult2*100)

main()                      # call the function main

