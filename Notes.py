# #this is working
# print("Hello World")
#
# # Marcos Cruz
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print # this makes a new line. In python 3.6, it looks like: print()
# print("See if you can figure this out")
# print(5 % 3)
# car_name = "Marcos Mobile"
# car_type = "Tesla model X"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline printing
# print("I have a car called the %s" % car_name)
# print("I have a car called the %s. It's  a %s." % (car_name, car_type))
#
# #Asking for input
# name = input ("What is your name?") #In python 3, it is just called input
# print("Hello %s." % name)
#
# Age = input ("How old are you?")
# print("%s?! your really that old!!!") % Age

# Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()

def say_hi(name):   # name is a perameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("marcos")


def print_age(name, age):
    print("%s is %d years old." % (name, age))
    age += 1  # age = age + 1
    print("Next year, they will be %d" %age)


print_age("marcos", 14)


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
    elif percentage >= 50:
        return "F"
    
