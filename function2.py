def findsmallest(x, y, z):
    if (x < y) and (x < z):
        return x;
    elif (y < z) and (y < x):
        return y;
    elif (z < x) and (z < y):
        return z;

print(findsmallest(5,3,4))

def sheep_call(vowel, count):
    for i in range(count):
        print (vowel)
        
sheep_call('b', 2)

