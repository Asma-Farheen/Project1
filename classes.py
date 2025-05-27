class Pets(object):
    def __init__(self, species, name):
        self.species = species
        self.name = name
my_cat = Pets(species="cat",name="tommy")
print(my_cat)
print(my_cat.name)
