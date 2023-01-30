#importing Python libraries
import time 
import string
import random 

#Defining Password Length
password_length = 8 

#Generating password of 8 characters
password_characters = string.ascii_letters + string.digits 
password_characters += string.punctuation 
password_characters = ''.join(random.sample(password_characters,password_length ))

#attempting to crack the password
try: 
    guess = ''
    while (guess != password_characters): 
        guess = input('Guess the Password: ') 
        if (guess == password_characters): 
            print('Password Cracked!') 
        else: 
            print('Wrong Password') 
            time.sleep(2)

except KeyboardInterrupt: 
    print('Exiting Program') 
    exit()