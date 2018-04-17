# Dealing with strings
strTwo = "ThIs iS a VeRY oDd sEnTenCE"
lowercase = strTwo.lower()
print(lowercase)
','''

# Dictionaries - Made up of key: Value pairs
dictionary = {'name': 'Marcos', 'age': 14, 'height': 5 * 10 + 6}

# Accessing dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Adding to a dictionary
dictionary['weight'] = 280
print(dictionary)


large_dictionary = {
    'CA': 'California',
    'FL': 'Florida',
    'Oh': 'Ohio'
}

print(large_dictionary)

larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacramento',
        "Los Angeles"
    ],
    'FL': [
        'Tampa',
        "Orlando",
        "Miami"
    ],
    'OH': [
        "Cleavland",
        "Cincinnati"
    ]
}


print(larger_dictionary['FL'])
print(larger_dictionary["FL"][2])

print(larger_dictionary['OH'])
print(larger_dictionary["OH"][1])


largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

print(largest_dictionary['NY']['POPULATION'])
print(largest_dictionary['NY']['NAME'])
current_node = largest_dictionary['CA']
print(current_node)


















