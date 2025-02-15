class Pet:
    allowed = ["cat", "dog", "fish", "rat", "parrot"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# tony = Pet("Tony","tiger")
# dog.species = "tiger"
# print(cat.set_species("rat"))
# print(cat.species)
# Pet.allowed.append("pig")
# print(Pet.allowed)
# print(cat.set_species("pig"))
# print(cat.species)
cat.allowed = ["turtle", "bear"]
print(cat.allowed)
print(Pet.allowed)
