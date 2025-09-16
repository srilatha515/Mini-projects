import random

random_number=random.randint(1,500)
while True:
    try:
        guess=int(input("random number between 1 to 500 : "))
        
        if guess < random_number:
            print("too low")
        elif guess > random_number:
            print("too_high")
        else:
            print("congrats!! you are guess is correct")
            break
    except:
        print("please select valid option")
