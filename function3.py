import random
def validate_password(password):
                
    #set up a variable (named counter) equal to 0
    #use a for loop to walk through the string
    #increment the counter
    #(outside loop) check if the counter is bigger ot equal to 8,print result
    length = 0
    for i in password:
        length += 1
    if length < 8:
        print("This password is not atleast 8 characters long")
    if length >= 8:
        print("This password IS atleast 8 characters long")
        
        
    if any(c.isupper() for c in password):
        print("This string has an uppercase letter")
    else:
        print("This string doesn't have an uppercase letter")
    
    #have a for loop that walks through the word
    #check if the letter you're looking at is 1 or 2 or 3 ect.
    #if it is, print yes
    #id not, print no
    for i in password:
        if i == '1'or i == '2'or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8'or i == '9':
            print("the string has a number")
        #elif i != '1'or i != '2'or i != '3' or i != '4' or i != '5' or i != '6' or i != '7' or i != '8'or i != '9':
            #print("the string doesnt have a number")
    

validate_password("pas3s")
validate_password("Charact1rssss")


def CheckPrime(number):
    Prime = True;
    if (number%2 == 0):
        Prime = True;
    else:
        Prime = False
    return Prime;
    
print(CheckPrime(36))

def guess_number():
    gameover = False
    
    randNum = random.randrange(100)
    print(randNum)
    while gameover == False:
        number = (int(input("Guess a number between 1-100")))
        if number == randNum:
            print("You guessed it right")
            gameover = True
        elif number < randNum:
            print("Too low,guess higher")
        elif number > randNum:
            print("Too high, guess lower")


guess_number()


