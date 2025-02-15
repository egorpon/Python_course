class Human:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self._age = age

  # def get_age(self):
  #   return self._age
  
  # def set_age(self,new_age):
  #   if new_age > 0:
  #     self._age = new_age
  #   else:
  #     self._age = 0

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if value > 0:
      self._age = value
    else:
      raise ValueError ("Age can't be negative!")

  @property
  def full_name(self):
    return f"{self.first} {self.last}"
  
  @full_name.setter
  def full_name(self,name):
    self.first,self.last = name.split(" ")


jane = Human("Jane", "Smith", 27)
print(jane.age)
jane.age = 12
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Cook"
print(jane.__dict__)