import keyword

def contains_keyword(*args):
  for item in args:
    if keyword.iskeyword(item):
      return True
    return False
print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))