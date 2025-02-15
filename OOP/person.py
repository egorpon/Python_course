class Person:
  def __init__(self):
    self.name = "Tony"
    self._secret = "hi!"
    self.__msg = "I like turtles!" 
    self.__lol = "HAHAHAHAHAAH"
  # def doorman(self, guess):
  #   if guess == self._secret:
  #     let them in

p = Person()
print(p.name)
print(p._secret)
# print(dir(p))
print(p._Person__msg)
print(p._Person__lol)

