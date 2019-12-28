class dog():

    def __init__(self, name, age, toy):
        self.name = name
        self.age = age
        self.toy = toy
        self.type = 'shiba'

    def sit(self):
        print(self.name.title() + " is sitting.")

    def rollover(self):
        print(self.name.title() + " is rolled.")

    def birthday(self):
        self.age += 1

    def intro(self):
        print(self.name.title() + ' ' + str(self.age) + ' ' + self.type)

    def playtoy(self):
        print("he is playing " + self.toy.name.title() + '(' + self.toy.color + ')')

class smallDog(dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age, toy)

    def namechange(self,newname):
        self.name = newname

    def rollover(self):
        print("small dog cannot rollover")

class Toy():
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.power = 10

    def intro(self):
        print(self.name.title() + ' ' + str(self.power) + ' ' + self.color)

toy1 = Toy('zz','red')
new_dog = dog('andy',14,toy1)
new_dog.sit()
new_dog.rollover()

new_dog.intro()

new_dog.age += 1
new_dog.intro()

new_dog.birthday()
new_dog.intro()
new_dog.playtoy()

new_smalldog = smallDog('city', 2, toy1)
new_smalldog.intro()
new_smalldog.birthday()
new_smalldog.intro()
new_smalldog.namechange('gig')
new_smalldog.intro()
new_smalldog.rollover()
new_smalldog.playtoy()

