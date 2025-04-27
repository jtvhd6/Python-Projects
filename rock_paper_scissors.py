import random

while (p1 := input("\nPlater 1: Please type Rock, Paper, or Scissors! ('q' to quit): ").lower()) != 'q':
    if p1 not in ["rock", "paper", "scissors"]:
        print("\nYou have typed an Invalid choice!"); continue
    p2 = random.choice(["rock", "paper", "scissors"])
    print(f"\nPlayer 1: {p1}\nPlayer 2: {p2}")
    print("\nYou Tied!" if p1 == p2 else "\nYou win!" if (p1, p2) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")] else "\nYou lose!")

print("\nHave a great day!\n")