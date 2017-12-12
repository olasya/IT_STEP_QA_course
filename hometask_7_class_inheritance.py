class Animal(object):

    def __init__(self, tail = 1, paw = 4, wool = True):
        self.tail = tail
        self.paw = paw
        self.wool = wool 

class Dog(Animal):
    def __init__(self, tail = 1, paw = 4, wool = True):
        Animal.__init__(self, tail, paw, wool)

    def say_something(self):
        return 'Woof-woof'

class Cat(Animal):
    def __init__(self, tail = 1, paw = 4, wool = True):
        Animal.__init__(self, tail, paw, wool)

    def say_something(self):
        return 'Meow - meow'

class Sphynx(Cat):
    def __init__(self, tail = 1, paw = 4, wool = False):
        Cat.__init__(self, tail, paw, wool)
        # self.wool = False

    def say_something(self):
        return 'murr-murr'

class Rooster(Animal):
    def __init__(self, tail = 1, paw = 2, wool = False):
        Animal.__init__(self, tail, paw, wool)
        # self.paw = 2
        # self.wool = False

    def say_something(self):
        return 'Cocorico'

some_animal = Animal()
dog_animal = Dog()
kitty = Cat()
cat_sphynx = Sphynx()
roosty = Rooster()

print some_animal.tail, some_animal.paw, some_animal.wool
print dog_animal.tail, dog_animal.paw, dog_animal.wool
print dog_animal.say_something()
print kitty.tail, kitty.paw, kitty.wool
print kitty.say_something()
print cat_sphynx.tail, cat_sphynx.paw, cat_sphynx.wool
print cat_sphynx.say_something()
print roosty.tail, roosty.paw, roosty.wool
print roosty.say_something()

        

        

        
        