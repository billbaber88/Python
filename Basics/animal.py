class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 0

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 10
        return self

    def display_health(self):
        print "My name is " + str(self.name)



class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

    def display_health(self):
        print "I have "+str(self.health) +" health reamining. Please don't let me die"

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -=10
        return self

    def display_health(self):
        print "I have "+str(self.health)+ " health reamining. I'm going to fly away and burn Westeros before you kill me from exhaustion."

dog = Dog('rover')
Drogon = Dragon('Drogon')

dog.walk().walk().walk().run().run().pet().display_health()

Drogon.fly().fly().fly().fly().fly().fly().run().display_health()