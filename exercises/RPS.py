from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:

  print(f"Player score: {player_wins} Computer score: {computer_wins}")
  print("Rock...")
  print("Paper...")
  print("Scissors...")
  player1 = input("Player, Make your move: ").lower()
  if player1 == "quit" or player1 == "q":
     break

  rand_num = randint(0,2)
  if rand_num == 0:
    computer = "rock"
  elif rand_num == 1:
    computer = "paper"
  else:
    computer = "scissors"
  print(f"Computer plays: {computer}")

  if player1 == computer:
    print("It's a tie!")

  elif player1 == "rock":
      if computer == "scissors":
          print("Player wins!")
          player_wins+=1
      elif computer == "paper":
          print("Computer wins!")
          computer_wins+=1

  elif player1 == "paper":
    if computer == "rock":
        print("Player wins!")
        player_wins+=1
    elif computer == "scissors":
        print("Computer wins!")
        computer_wins+=1


  elif player1 == "scissors":
    if computer == "rock":
        print("Computer wins!")
        computer_wins+=1
    elif computer == "paper":
        print("Player wins!")
        player_wins+=1
  else:
    print("Please enter a valid move!")

    
if player_wins > computer_wins:
   print("CONGRATS YOU WON!")
elif player_wins == computer_wins:
   print("IT'S A TIE!")
else:
   print("OH NO :( THE COMPUTER WON...")
print(f"Final scores... Player... {player_wins} Computer... {computer_wins}")