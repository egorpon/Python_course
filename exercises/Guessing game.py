import random 
random_number = random.randint(1,20)
while True:
  
  guess_num = int(input("Guess a number between 1 and 10: "))
  if guess_num <random_number:
      print("Too low, try again!")
  elif guess_num >random_number:
      print("Too high, try again!")
  else:
    print("You guessed it! You won!")
    a = input("Do you want to keep playing? (y/n)")
    if a == "y":
         random_number = random.randint(1,10)
         guess_num = None
    else:
       print("Thank you! See you again!")
       break
  