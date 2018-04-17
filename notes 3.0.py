the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Tacos"]

print(shopping_list[0])

print(len(shopping_list))

# Going through a list
for item in shopping_list:
    print(item)

for number in the_count:
    print(number)

for number in the_count:
    print(number * 2)

len(shopping_list)  # Gives me the length of the list)
range(3)  # Gives a list of the number 0 through 2
range(len(shopping_list))  # a List if every index in a list

for number in range(len(shopping_list)):
    item = shopping_list[number]
    print("The item at index %d is %s" % (number, item))

# Turn things into a list
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)

str1 = "Hello World!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

# Add things to a list
shopping_list.append("cereal")
print(shopping_list)

# the string class
import  string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# dealing with strings
strTwo = "tHiS iS a VeRY oDd"
lowercase = strTwo.lower()
print(lowercase)

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except keyerror
     
    else:
        print('Command not Recognized')
















