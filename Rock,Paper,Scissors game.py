import random
name=input("What is your name? ")
options=("rock","paper","scissors")
running=True
while running:
  player=None
  computer=random.choice(options)
  while player not in options:
    player=input("Enter a choice (rock, paper, scissors):- ")
    print(f"you have chosen {player}:")
    print(f"computer has chosen :{computer}")
    if player==computer:
      print("It's a tie!")
    elif player=="rock" and computer=="scissors":
      print("You win!")
    elif player=="paper" and computer=="rock":
      print("You win!")
    elif player=="scissors" and computer=="paper":
      print("You win!")
    else:
      print("You lose!")
    if not input("Play again? (y/n):- ").lower()=="y":
      running=False
print(f"Thanks for playing {name}!!")
    
  