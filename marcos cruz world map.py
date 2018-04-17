world_map = {
    'WStadium': {
        'NAME': "West of Stadium",
        'DESCRIPTION': "You west of a big stadium",
        'PATHS': {
            'NORTH': 'NStadium',
            'SOUTH': 'South of Stadium'
        }
    },
    'NSTADIUM': {
        'NAME': 'North of Stadium',
        'DESCRIPTION': "announcers room ",
        'PATHS': {
            'SOUTH': 'West of Stadium'

        }
    },
    'SSTADIUM': {
        'NAME': 'South of Stadium',
        'DESCRIPTION': "Way to go to locker rooms and storage places",
        'PATHS': {
            'North': 'Soccer Field'
        }
    },
    'ESTADIUM': {
        'NAME': 'Eest of Stadium',
        'DESCRIPTION': "way to go to soccer field or locker rooms",
        'PATHS': {
            'West': 'Soccer Field'
        }
    },
    'Soccer Field': {
        'NAME': 'Starting Point',
        'DESCRIPTION': "Where you start the game",
        'PATHS': {
            'NORTH': 'North of stadium'
            'East'
            'West'
            'South'
        }
    },
    'ANNOUNCERS': {
        'NAME': 'Announcers Room',
        'DESCRIPTION': "People that explain and see the whole game are in the announcers room.",
        'PATHS': {
            'NORTH': 'North of stadium'
        }
    },
    'SROOM2': {
        'NAME': 'Secret Room #2',
        'DESCRIPTION': "Secret items that will help you throughout the whole game",
        'PATHS': {
            'NORTH': 'WESTHOUSE'
        }
    },
    'SROOM1': {
        'NAME': 'Secret Room #1',
        'DESCRIPTION': "Secret items that will help you throughout the whole game",
        'PATHS': {
            'NORTH': 'East of stadium'
        }
    },
    'SROOM3': {
        'NAME': 'Secret Room #3',
        'DESCRIPTION': "Secret items that will help you throughout the whole game",
        'PATHS': {
            'NORTH': 'West of stadium'
        }
    },
    'LROOM #1': {
        'NAME': 'Locker Room #1',
        'DESCRIPTION': "where different teams get ready and talk before a game",
        'PATHS': {
            'NORTH': 'CELLAR1'
        }
    },
    'LROOM #2': {
        'NAME': 'Locker Room #2',
        'DESCRIPTION': "where different teams get ready and talk before a game",
        'PATHS': {
            'NORTH': 'CELLAR2'
        }
    },
    'CELLAR1': {
        'NAME': 'Cellar #1',
        'DESCRIPTION': "where they keep extra equipment ",
        'PATHS': {
            'SOUTH': 'STORAGE1'
        }
    },
    'CELLAR2': {
         'NAME': 'Cellar #2',
         'DESCRIPTION': "where they keep extra equipment ",
         'PATHS': {
             'SOUTH': 'STORAGE2'
         }
    },
    'STORAGE1': {
        'NAME': 'Storage #1',
        'DESCRIPTION': "keeps things that are new or also the lost and found",
        'PATHS': {
            'SOUTH EAST': 'East of stadium'
        }
    },
    'STORAGE2': {
        'NAME': 'Storage #2',
        'DESCRIPTION': "keeps things that are new or also the lost and found",
        'PATHS': {
            'NORTH': 'West of stadium'
        }
    },
 },

current_node = world_map['Soccer Field']
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
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')
    print()
