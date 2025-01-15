def factorial(n):
    #Base case: the factorial of 0 or 1 is 1 (return true)
    if n == 0 or n == 1:
        return 1;
    else:
        #recursive case : n multiplied by the factorial of n-1
        return n* factorial(n-1)
    
print(factorial(10))

def is_palindrome(word,left,right):
    #base case: if there is only one or no character left it's a palindrome. return true
    # do this by checking the left index versus the right... have they overlapped?
    if left == right:
        return True
    
    if word[left] != word[right]:
        return False
    
    return is_palindrome(word, left+1, right-1)

print(is_palindrome("amanaplanacanalpanama", 0, len("amanaplanacanalpanama") -1)) #output true
print(is_palindrome("hello", 0, len("hello") -1)) #output False
    
    #check if the characters at the current position are the same, if so return false
    
    #recursive call to move tword the middle of the string. move the left index over one to the right, and the right index back one towards the left
    
    
    
def print_pattern(n):
    if n > 0:
        for i in range(n):
            print("*", end = "")
        print()
        #recursive call with n-1
        print_pattern(n-1);
    
print_pattern(25)
