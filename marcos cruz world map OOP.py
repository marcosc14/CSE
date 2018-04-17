class Room(object):
    def __init__(self, name, north, east, south, west, up, down, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
field = Room('field', 'north_stadium', 'east_stadium', 'south_stadium', 'west_stadium', None, None,
             'You are in the center of the field.')
west_stadium = Room('West of Stadium', 'secret_room', 'field', None, None, None, None,
                    'You are now west of stadium')
north = Room('east of stadium', None, None, 'field', None, 'announcers_room', None,
             'You are now north of stadium')
south = Room('south of stadium', 'field', None, 'secret _room', None, None, None,
             'You are now south of Room')
east = Room('east of stadium', None, None, 'field', 'secret_room', None, None,
            'You are now east of stadium')
announcers_room = Room('announcers room', None, None, 'field', None, 'north_stadium', None,
                       'You are now in the announcers room')
secret_room1 = Room('secret room', 'south_stadium', None, None, None, None, None,
                    'You are now in the secret room')
secret_room2 = Room('secret room', 'east_stadium', None, None, None, None, None,
                    'You are in the second secret room')
secret_room3 = Room('secret room', None, None, 'west_stadium', None, None, None,
                    'You are now in the third secret room')
locker_room1 = Room('locker room', 'storage_room', None, None, None, None, None,
                    'You are now in the locker rooms')
locker_room2 = Room('locker room', 'cellar', None, 'storage_room', None, None, None,
                    'You are now in the second locker room')
cellar1 = Room('cellar', None, None, 'locker_room1', None, None, None,
               'You are now in the cellar')
cellar2 = Room('cellar2', None, None, 'locker_room2', None, None, None,
               'You are now in the second cellar')
storage_room1 = Room('storage room1', 'locker_room1', None, None, None, None, None,
                     'You are now in the storage room')
storage_room2 = Room('storage room2', 'cellar2', None, 'locker room2', None, None, None,
                     'You are now in the send storage room')
current_node = field
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_'). lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')
    print()
