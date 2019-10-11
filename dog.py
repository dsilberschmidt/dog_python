class Dog:
    species = 'caniche'

    def __init__(self, name, age):
            self.name = name
            self.age = age

bambi = Dog("Bambi", 5)
mikey = Dog("Rufus", 6)

print("{} is {} and {} is {}.".format(
    bambi.name, bambi.age, mikey.name, mikey.age))

if bambi.species == "mammcanichea1":
    print("{0} is a {1}!".format(bambi.name, bambi.species))

maia = Dog("Maia", 10)
mira = Dog("Mira", 18)
nur = Dog("Nur", 2)

def get_biggest_number (*args):
    print (max (*args))

