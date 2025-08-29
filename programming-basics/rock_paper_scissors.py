# rock_paper_scissors.py
import random

choices = ["rock", "paper", "scissors"]
user = input("Enter rock/paper/scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a Tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You Win! 🎉")
else:
    print("You Lose! ❌")
git add .
git commit -m "Added basic Python programs"
git push origin main
