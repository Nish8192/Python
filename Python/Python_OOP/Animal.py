class Animal(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def walk(self, x = 1):
        while(x>0):
            if(self.health <= 1):
                print self.name + " will die if he tries to walk. Don't kill " + self.name + " :("
                return self
            self.health -= 1
            x -= 1
        return self

    def run(self, x = 1):
        while(x>0):
            if(self.health <= 5):
                print self.name + " will die if he tries to run. Don't kill " + self.name + " :("
                return self
            self.health -= 5
            x -= 1
        return self
    def displayHealth(self):
        print self.name,':', self.health
        return self
class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)

    def pet(self, x = 1):
        while(x>0):
            self.health += 5
            x -= 1
        return self
class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)

    def fly(self, x = 1):
        while(x>0):
            if(self.health <= 10):
                print self.name + " will die if he tries to fly. Don't kill " + self.name + " :("
                return self
            self.health -= 10
            x -= 1
        return self
    def displayHealth(self):
        print "This is a dragon!: "
        super(Dragon, self).displayHealth()
        return self

Monster = Animal('HellBest')
Monster.walk(3)
Monster.run(300)
Monster.displayHealth()

Ghost = Dog('Ghost')
Ghost.walk(3)
Ghost.run(2)
Ghost.pet()
Ghost.displayHealth()

Drogon = Dragon('Drogon')
Drogon.walk(3)
Drogon.run(2)
Drogon.fly(50)
Drogon.displayHealth()
