import random
import string

def password_generator():
    length = int(input("Enter the length of the password:"))
    
    if length <=6:
        print("Password length should be at least 6.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"Generated password: {password}")
password_generator()