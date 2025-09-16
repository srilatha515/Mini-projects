import random

import string

def generate_password(min_length , numbers=True , special_chars=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_chars:
        characters+=special

    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or len(pwd) < min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        
        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        elif special:
            meets_criteria=meets_criteria and has_number
    
    return pwd

min_len=int(input("enter minimum length :"))
has_number=input("Do you want number (y/n)?: ").lower()
has_special=input("Do you want special character (y/n)>: ").lower()
pwd=generate_password(min_len,has_number,has_special)
print(pwd)
