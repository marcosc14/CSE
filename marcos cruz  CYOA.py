# -Import statements
# -Class definitions
# - items
# - characters
# - rooms
# - Instantiate classes
# - Controller


class Item(object):
    def __init__(self, name):
        self.name = name

    def drop(self):
        print("You dropped a %s." % self.name)

    def take(self):
        print("You took a %s." % self.name)


class Tool(Item):
    def __init__(self, name):
        super(Tool, self).__init__(name)

    def build(self):
        print("You build with your %s" % self.name)


class Hammer(Tool):
    def __init__(self, name, metal, description):
        super(Hammer, self).__init__(name)
        self.metal = metal
        self.description = description

    def smash(self):
        print("You smash with a %s" % self.name)


class Screw(Tool):
    def __init__(self, name, metal, description):
        super(Screw, self).__init__(name)
        self.metal = metal
        self.description = description

    def screwing(self):
        print("You could %s the nail" % self.name)


class Heal(Item):
    def __init__(self, name):
        super(Heal, self).__init__(name)

    def heal(self):
        print("You got %s" % self.name)


class MedKit(Heal):
    def __init__(self, name, description):
        super(MedKit, self).__init__(name)
        self.description = description

    def carry(self):
        print("Med kit carries %s" % self.name)


class Herbs(Heal):
    def __init__(self, name, description):
        super(Herbs, self).__init__(name)
        self.description = description

    def color(self):
        print("The herb is %s" % self.name)


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)

    def attack(self):
        print("My %s can attack" % self.name)

    def damage(self):
        print("My %s does a lot of damage" % self.name)


class Melee(Weapon):
    def __init__(self, name):
        super(Melee, self).__init__(name)

    def damage(self):
        print("My %s does a lot of dmg" % self.name)

    def metal(self):
        print("The %s on my melee is sharp" % self.name)


class Axe(Weapon):
    def __init__(self, name, description):
        super(Axe, self).__init__(name)
        self.description = description

    def damage(self):
        print("My %s does a lot of damage" % self.name)

    def metal(self):
        print("My %s metal is super strong" % self.name)


class Armor(Item):
    def __init__(self, name):
        super(Armor, self).__init__(name)

    def metal(self):
        print("The metal on my %s is super strong" % self.name)

    def shape(self):
        print("The shape of my %s is round" % self.name)


class BodyArmor(Armor):
    def __init__(self, name, description):
        super(BodyArmor, self).__init__(name)
        self.description = description

    def metal(self):
        print("The metal on my %s is hard and could stop anything" % self.name)

    def surface(self):
        print("The surface of my %s is flat but strong" % self.name)


class ShinGuard(Armor):
    def __init__(self, name, description):
        super(ShinGuard, self).__init__(name)
        self.description = description

    def foam(self):
        print("The foam helps the %s protect our shin from the ball" % self.name)

    def hard_plastic(self):
        print("The hard plastic in the %s helps the foam protect our shin" % self.name)


class Consumable(Item):
    def __init__(self, name):
        super(Consumable, self).__init__(name)

    def flavor(self):
        print("My %s has a lot of flavor" % self.name)


class Salad(Consumable):
    def __init__(self, name, description):
        super(Salad, self).__init__(name)
        self.description = description

    def flavor(self):
        print("My %s has a good flavor in it" % self.name)

    def bowl(self):
        print("My %s has a nice round bowl to hold it while i eat it" % self.name)


class Bacon(Consumable):
    def __init__(self, name, description):
        super(Bacon, self).__init__(name)
        self.description = description

    def flavor(self):
        print("The %s has a good taste to it" % self.name)

    def aroma(self):
        print("The aroma of the %s is good" % self.name)


class Key(Item):
    def __init__(self, name):
        super(Key, self).__init__(name)

    def aluminum(self):
        print("The aluminum of my %s is strong and it wont break when you put it in key whole" % self.name)


class Key1(Key):
    def __init__(self, name, description):
        super(Key1, self).__init__(name)
        self.description = description

    def aluminum(self):
        print("The aluminum of my %s is strong and it wont break when you put it in key whole" % self.name)

    def curves(self):
        print("The curves in my %s has to match the curves in the key hole in order to open" % self.name)


class Key2(Key):
    def __init__(self, name, description):
        super(Key2, self).__init__(name)
        self.description = description

    def aluminum(self):
        print("The aluminum of my %s is strong and it wont break when you put it in key whole" % self.name)

    def curves(self):
        print("The curves in my %s has to match the curves in the key hole in order to open" % self.name)


class Key3(Key):
    def __init__(self, name,  description):
        super(Key3, self).__init__(name)
        self.description = description

    def aluminum(self):
        print("The aluminum of my %s is strong and it wont break when you put it in key whole" % self.name)

    def curves(self):
        print("The curves in my %s has to match the curves in the key hole in order to open" % self.name)


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)

    def brand(self):
        print("The brand of my %s is fine its the best queality" % self.name)


class Jersey(Clothing):
    def __init__(self, name, description):
        super(Jersey, self).__init__(name)
        self.description = description

    def logo(self):
        print("The logo of my %s represents the club or country of the team" % self.name)

    def colors(self):
        print("The colors of my %s is bright" % self.name)


class Suit(Clothing):
    def __init__(self, name, description):
        super(Suit, self).__init__(name)
        self.description = description

    def silk(self):
        print("The silk of my %s is soft" % self.name)

    def brand(self):
        print("The brand of my %s cost a lot" % self.name)


class Character(object):
    def __init__(self, status_effect, alive, name, health, dmg, location):
        self.Inventory = []
        self.Status_Effect = status_effect
        self.alive = alive
        self.name = name
        self.health = health
        self.damage = dmg
        self.location = location

    def take_damage(self, amt):
        if self.health <= 0:
            print("%s is dead")
            return
        self.health -= amt
        if self.health <= 0:
            self.alive = False
            print("%s has died." % self.name)

    def attack(self, enemy):
        print("attack")
        if self.alive:
            print("You attacked %s" % self.name)
            enemy.take_damage(self.damage)
        else:
            print("%s is dead and cannot attack." % self.name)

    def look(self):
        print(self.location.name)

    def drop(self, item):
        self.Inventory.remove(item)
        print("dropped")

    def take(self, item):
        self.Inventory.append(item)
        print("pick up")

    def kick(self, item):
        self.name(item)
        print("kick")

    def move(self, direction):
        self.location = globals()[getattr(self.location, direction)]

class Room(object):
    def __init__(self, name, north, east, south, west, up, down, description, characters, items=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.characters = characters
        self.items = items
        if items is None:
            items = []

# Items


axe = Axe('axe', 'This is a shiny axe.')
hammer = Hammer('hammer', None, 'There is a big heavy hammer')
screw = Screw('screw', None, 'There is a pointy screw')
medkit = MedKit('medkit', 'Medkit gives 20+ HP')
herbs = Herbs('herbs', 'herbs give 10+ HP')
Body_armor = BodyArmor('body_armor', 'bodyarmor gives you 10+ HP')
shinguard = ShinGuard('shinguard', 'shinguard give you 5+ HP')
salad = Salad('salad', 'eating salads give you 2.5+ HP')
bacon = Bacon('bacon', 'eating bacon gives you 2.5+ HP')
key1 = Key1('key1', 'There is key1 it opens secret door 1')
key2 = Key2('key2', 'There is key2 it opens secret door 2')
key3 = Key3('key3', 'There is key3 it opens secret door 3')
jersey = Jersey('jersey', 'There is a blue jersey')
suit = Suit('suit', 'There is a silky suit')

# Characters
Marcos = Character("good", True, "Marcos", 10, 3, None)
Edgar = Character("bad", True, "Edgar", 10, 3, None)
Messi = Character("good", True, "Messi", 10, 3, None)
Pele = Character("bad", True, "Pele", 10, 3, None)
Neymar = Character("good", True, "Neymar", 10, 3, None)
Suarez = Character("good", True, "Suarez", 10, 3, None)
Ronaldo = Character("bad", True, "Ronaldo", 10, 3, None)

# Initialize Rooms
field = Room('field', 'north_stadium', 'east_stadium', 'south_stadium', 'west_stadium', None, None,
             'You are in the center of the field. There\'s a axe here.', None, [axe])
west_stadium = Room('West of Stadium', 'secret_room', 'field', None, None, None, None,
                    'You are now west of stadium. There\'s a jersey here. Messi is in this room.', [Messi], [jersey])
north_stadium = Room('north of stadium', None, None, 'field', None, 'announcers_room', None,
                     'You are now north of stadium. There\'s some juicy bacon.', None, [bacon])
south_stadium = Room('south of stadium', 'field', None, 'secret _room', None, None, None,
                     'You are now south of stadium. There\'s some pair of shinguard\'s', None, [shinguard])
east_stadium = Room('east of stadium', None, None, 'field', 'secret_room', None, None,
                    'You are now east of stadium. There is a screw here.', None, [screw])
announcers_room = Room('announcers room', None, None, 'field', None, 'north_stadium', None,
                       'You are now in the announcers room. There\'s a heavy hammer here. Edgar the ogor is here.'
                       ' Attack',[Edgar], [hammer])
secret_room1 = Room('secret room', 'south_stadium', None, None, None, None, None,
                    'You are now in the secret room. There\'s green salad here. Pele is here. Attack', [Pele], [salad])
secret_room2 = Room('secret room', 'east_stadium', None, None, None, None, None,
                    'You are in the second secret room. There\'s a medkit in here. Neymar is here get the medkit from '
                    'him. don\'t engaged', [Neymar], [medkit])
secret_room3 = Room('secret room', None, None, 'west_stadium', None, None, None,
                    'You are now in the third secret room. There is a suit in here. Ronaldo is in here take the suit'
                    ' from him', [Ronaldo], [suit])
locker_room1 = Room('locker room', 'storage_room', None, None, None, None, None,
                    'You are now in the locker rooms.There\'s key1 in here', None, [key1])
locker_room2 = Room('locker room', 'cellar', None, 'storage_room', None, None, None,
                    'You are now in the second locker room. There\'s key2 in here', None, [key2])
cellar1 = Room('cellar1', None, None, 'locker_room1', None, None, None,
               'You are now in the cellar. There\'s key3 in here', None, [key3])
cellar2 = Room('cellar2', None, None, 'locker_room2', None, None, None,
               'You are now in the second cellar. Suarez is in here. Attack', [Suarez], None)
storage_room1 = Room('storage room1', 'locker_room1', None, None, None, None, None,
                     'You are now in the storage room. There\'s some herbs in here take them', None, [herbs])
storage_room2 = Room('storage room2', 'cellar2', None, 'locker room2', None, None, None,
                     'You are now in the send storage room. There\'s body armor in here take it', None, [Body_armor])
Marcos.location = field
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    #   Room Descriptions
    print(Marcos.location.name)
    print(Marcos.location.description)
    command = input('>_') .lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            Marcos.move(command)
        except KeyError:
            print("You cannot go this way.")

    elif 'take' in command:
        take_name = command[5:]
        found = False
        for item in Marcos.location.items:
            if take_name == item.name.lower():
                if Marcos.take(item):
                    found = item
        if found is False:
            print("You didn't find the item.")
        else:
            Marcos.location.items.remove(found)
    #
    # elif 'drop' in command:
    #     taken_name = command[5:]
    #     found = False
    #      for item in Messi.location.items:
    #
    else:
        print('Command not Recognized')
    print()
