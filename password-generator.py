import random #this module used to generate random numbers
import math

def generate_password(length):
    password = ""
    #the function chooses a characters for the password from this character string
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    for i in range(length):
        new= math.floor(random.random() * len(characters)) #this line generates a random number between 0 and the length of the characters string minus 1
        password += characters[new]
    return password

password_length = int(input("Enter password length: "))
generated_password = generate_password(password_length)
print("Your password is:", generated_password)
