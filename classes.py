import random
#Write a python class named "Evan". 
#Evan has three variables: tiredness, hunger, and grumpiness.
#Evan has three functions: SnarkyRemark(), Code(), and PrintInfo().
#The constructor takes values for the first two variables as parameters and randomizes the third (each should be something between 1-100).
#When called, SnarkyRemark randomly prints one of three phrases to the screen, like "you suck", "javascript is the best", or "here's some mayo".
#Code() just prints random Javascript jibberish to the screen, but decreases grumpiness and increases hunger. PrintInfo prints the contents of each of the variables.

class Even:
    def __init__(self, t, h):
        self.tiredness = t
        self.hunger = h
        self.grumpiness = random.randrange(30, 100)
    def SnarkyRemark(self):
        if self.grumpiness < 33:
            print("here's some mayo")
        elif self.grumpiness < 66:
            print("javascript is the best")
        else:
            print("you sucK")
        
    def Code(self):
        print("code code code ... javascrpit ... jiberish jiberish... ")
        self.grumpiness -= 30
        self.hunger += 40
    def PrintInfo(self):
        print("tiredness: ", self.tiredness)
        print("hunger: ",self.hunger)
        print("grumpiness: ",self.grumpiness)

#Instantiate one Evan object and call each of the functions to demonstrate how they work. 
    
Even1 = Even(100, 20)
Even1.SnarkyRemark()
Even1.PrintInfo()
Even1.Code()
Even1.PrintInfo()
    
