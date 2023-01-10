#modules
import secrets 
import string

#loop
while True:
    #How many characters your password will be?
    characters_number_user = input('How many characters your password will be? ')
    x = int(characters_number_user)


    #Code
    password = ''.join((secrets.choice(string.ascii_letters+string.digits+string.punctuation)) for i in range(x))
    print(password)