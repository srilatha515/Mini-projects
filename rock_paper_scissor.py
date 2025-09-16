import random

choices=('r','s','p')

def get_user_choice():
    while True:
        user_choice = input("Rock,paper or scissors? (r/s/p): ").lower()
        if user_choice not in choices:
              return user_choice
        else:
              print("invalid choice")
              continue
    
def display_choice(user_choice,computer_choice):
    print(f'you choose {user_choice}')
    print(f'computer choose {computer_choice}')

def determine_winner(user_choice,computer_choice):
    while True:
          if user_choice == computer_choice:
                print("Tie!!")
          elif((user_choice=='r' and computer_choice=='s') or(user_choice=='s' and computer_choice=='p') or(user_choice=='p' and computer_choice=='r')):
               print("you win")
          else:
              print("you lose")
        

def paly_game():
     while True:
         user_choice=get_user_choice()
    
         computer_choice = random.choice(choices)
         display_choice(user_choice,computer_choice)
         determine_winner(user_choice,computer_choice)
        
         should_continue=input("yo want to continue? (y/n): ").lower()
         if should_continue=="n":
             break
             

    


