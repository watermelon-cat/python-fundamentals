#Alejandro Elias
#1/24/25
#Write a function that calculates the surface area of a sphere given its radius. Call the function inside a print statement.
import math
def spherearea(r):
    print (4*math.pi*r**2)

spherearea(5)
#Write function ChangeChecker(). This function takes an integer parameter and checks if it's divisible by five.
#If it is, it prints "no pennies needed". If it's not, it prints "you'll need pennies for this!". Call the function twice; once with 25, and another time with 17.
def ChangeChecker(num):
    if (num%5 == 0):
        print("no pennies needed")
    else:
        print("you'll need pennies for this!")
ChangeChecker(25)
ChangeChecker(117)
# Check Prime Number: Develop a function to check whether a given number is prime or not.
#Use a loop to try dividing the number by all integers from 2 up to the square root of the number. If it is divisible by any number other than 1 and itself, it is not prime.
def CheckPrime(number):
    Prime = True;
    for i in range(2, number):
        if (number%i == 0):
            Prime = False;
    return Prime;

    
print(CheckPrime(37))
    
