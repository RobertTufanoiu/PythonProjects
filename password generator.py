import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pswd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pswd) < min_length:
        new_character = random.choice(characters)
        pswd += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special

    return pswd


min_length = int(input("Enter the minimum length of the password: "))
has_number = input("Do you want the password to contain numbers? (y/n) ").lower() == "y"
has_special = input("Do you want the password to contain special characters? (y/n) ").lower() == "y"

pswd = generate_password(min_length, has_number, has_special)
print("The generated password is: ", pswd)








