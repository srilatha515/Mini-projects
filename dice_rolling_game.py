import random

while True:
    choice=input("dice is roll? (y/n):").lower()
    if choice == "y":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        dice3=random.randint(1,6)
        print(f'({dice1},{dice2},{dice3})')
    elif choice =="n":
        print("thanks for playing")
        break
    else:
        print("invalid option")