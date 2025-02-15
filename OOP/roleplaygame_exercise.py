class Character:
  def __init__(self, name, hp, level):
    self.name = name
    self.hp = hp
    self.level = level
  def __repr__(self):
    return f"{self.name} got a {self.hp} healtpoint and {self.level} level"

class NPC(Character):
  def __init__(self,name,hp,level):
    super().__init__(name,hp,level)

  def speak(self):
    return "I heard there were monsters running around last night!"
    

villager = NPC("Tom", 87, 10)

print(villager.name)
print(villager.hp)
print(villager.level)

print(villager.speak())

print(villager)