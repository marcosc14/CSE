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
    def __init__(self, name, metal):
        super(Hammer, self).__init__(name)
        self.metal = metal

    def smash(self):
        print("You smash with a %s" % self.name)


class Screw(Tool):
    def __init__(self, name, metal):
        super(Screw, self).__init__(name)
        self.metal = metal

    def screwing(self):
        print("You could %s the nail" % self.name)


class Heal(Item):
    def __init__(self, name):
        super(Heal, self).__init__(name)

    def heal(self):
        print("You got %s" % self.name)


class MedKit(Heal):
    def __init__(self, name):
        super(MedKit, self).__init__(name)

    def carry(self):
        print("Med kit carries %s" % self.name)


class Herbs(Heal):
    def __init__(self, name):
        super(Herbs, self).__init__(name)

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
    def __init__(self, name):
        super(Axe, self).__init__(name)

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
    def __init__(self, name):
        super(BodyArmor, self).__init__(name)

    def metal(self):
        print("The metal on my %s is hard and could stop anything" % self.name)

    def surface(self):
        print("The surface of my %s is flat but strong" % self.name)


class ShinGuard(Armor):
    def __init__(self, name):
        super(ShinGuard, self).__init__(name)

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
    def __init__(self, name):
        super(Salad, self).__init__(name)

    def flavor(self):
        print("My %s has a good flavor in it" % self.name)

    def bowl(self):
        print("My %s has a nice round bowl to hold it while i eat it" % self.name)


class Bacon(Consumable):
    def __init__(self, name):
        super(Bacon, self).__init__(name)

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
    def __init__(self, name):
        super(Key1, self).__init__(name)

    def aluminum(self):
        print("The aluminum of my %s is strong and it wont break when you put it in key whole" % self.name)

    def curves(self):
        print("The curves in my %s has to match the curves in the key hole in order to open" % self.name)


class Key2(Key):
    def __init__(self, name):
        super(Key2, self).__init__(name)

    def aluminum(self):
        print("The aluminum of my %s is strong and it wont break when you put it in key whole" % self.name)

    def curves(self):
        print("The curves in my %s has to match the curves in the key hole in order to open" % self.name)


class Key3(Key):
    def __init__(self, name):
        super(Key3, self).__init__(name)

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
    def __init__(self, name):
        super(Jersey, self).__init__(name)

    def logo(self):
        print("The logo of my %s represents the club or country of the team" % self.name)

    def colors(self):
        print("The colors of my %s is bright" % self.name)


class Suit(Clothing):
    def __init__(self, name):
        super(Suit, self).__init__(name)

    def silk(self):
        print("The silk of my %s is soft" % self.name)

    def brand(self):
        print("The brand of my %s cost a lot" % self.name)
