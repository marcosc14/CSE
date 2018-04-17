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


Marcos = Character("good", True, "Marcos", 10, 3, None)
Messi = Character("good", True, "Messi", 10, 3, None)
Pele = Character("good", True, "Pele", 10, 3, None)
Neymar = Character("good", True, "Neymar", 10, 3, None)
Suarez = Character("good", True, "Suarez", 10, 3, None)
Ronaldo = Character("good", True, "Ronaldo", 10, 3, None)

