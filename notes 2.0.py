# print("Hello world")
# # This is a new line of code

# a = 4
# b = 3
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print()
# print("Try to figure out how this works")
# print(13 % 5)
#
# # the "%" sign is a modulus. It finds the remainder.
#
# car_name = "The Wiebe Mobile"
# car_type = "BMW"
# car_cylin
#
# # Mr. Wiebe
#ders = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s." % (car_name, car_type)) # watch the order
#
# # Here is where we get a little fancy
# print("What is your name?")
# name = input(">_ ")
# print("Hello %s." % name)
#
# age = input("How old are you?")
# print("%s?! That's really old. You belong in a retirement home." % age)

# Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()


def say_hi(name):  # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old." % (name, age))
    age += 1  # age = age + 1
    print("Next year, they will be %d" % age)


print_age("John", 15)


def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))

# If statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


'''Write a function called "happy_bday"
that "sings" (prints) Happy birthday
It must take one parameter called "name"
'''


def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday to " + name + ",")
    print("Happy birthday to you" + ".")

happy_bday("John")


# Loops

for num in range(10):
    print(num + 1)


a = 1
while a <= 10:
    print(a)
    a += 1


# Random Numbers

import random  # This should be on line 1
print(random.randint(0, 100))







# Removing things from list
shopping_list.remove("soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)