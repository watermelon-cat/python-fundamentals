import math
def calculate_circumference(radius):
    return(2*math.pi*radius)
print(calculate_circumference(4))

def zpattern(n):
    for a in range(1, n, 2):
        print(a, end = " ")
    for b in range(n, 0, -2):
        print(b, end = " ")
zpattern(10)
zpattern(23)
zpattern(15)

def sums3s5s(o):
    sums = 0
    for i in range(o+1):
        if i % 3 == 0 or i % 5 == 0:
            sums += i
    return sums

print(sums3s5s(9)) #3+5+6+9 = 23
print(sums3s5s(14)) #3+4+6+9+10+12 = 45


