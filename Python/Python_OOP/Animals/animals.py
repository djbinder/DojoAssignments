class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self 

    def run(self):
        self.health = self.health - 5
        return self 

    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def set_health(self):
        self.health = 150
        return self
    
    def pet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    def set_health(self):
        self.health = 170
        return self
    
    def fly(self):
        self.health = self.health - 10
        return self
    

frog = Animal("Kermit",100)
frog.display_health()
print ("\n")

buddy = Dog("Buddy",100)
buddy.set_health()
buddy.set_health().walk().walk().walk().run().run().pet().display_health()
print "My Dog Name is: ", buddy.name
print "My Current Health is: ", buddy.health
print ("\n")

fire = Dragon("fire",100)
fire.set_health().fly()
print "My Dragon Name is: ", fire.name
print "My Current Health is: ", fire.health
