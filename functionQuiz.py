def countdown_launch(n):
    for b in range (n + 1):
        print(b)
        n -= 1
    print("liftoff")
    
countdown_launch(5)

def has_digit(password):
    for i in password:
        if i == '1'or i == '2'or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8'or i == '9':
            return("the string has a number")
            
            
print(has_digit("number"))
print(has_digit("nu4b3r"))

def trapezoid_area(base1, base2, height):
    return(((base1 + base2) * height) // 2)

print(trapezoid_area(9, 15, 6))
