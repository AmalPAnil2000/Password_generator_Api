# utils.py
import random
import string

def generate_password(length=12, choices=['uppercase', 'lowercase', 'digits', 'special']):
    characters = ''
    
    for choice in choices:
        if choice == 'uppercase':
            characters += string.ascii_uppercase
        elif choice == 'lowercase':
            characters += string.ascii_lowercase
        elif choice == 'digits':
            characters += string.digits
        elif choice == 'special':
            characters += string.punctuation

    if not characters:
        raise ValueError("No character set selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
