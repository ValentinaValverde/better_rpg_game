class Element:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def info(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    
    def attack(self, opponent):
        print(" ")
        print("%s has attacked %s!" % (self.name, opponent.name))
        opponent.health -= self.power
        print("%s now has %s health!" % (opponent.name, opponent.health))
        print(" ")


#element types are : fire, water, air, and earth

class Fire(Element):
    def fire(self):
        print("🔥")


class Water(Element):
    def water(self):
        print("💧")


class Air(Element):
    def air(self):
        print("💨")


class Earth(Element):
    def earth(self):
        print("🌱")
