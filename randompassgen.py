# TASK 3 - RANDOM PASS GEN

# importing modules
import random
import string

# function for password generation
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# input legnth for video
password_length = int(input("Enter the legnth of Password:"))  
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
