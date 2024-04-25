import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
