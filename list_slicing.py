#print every 3 letters
list = ['d', 'r', '^', 'o', ']', 'Z', 'g', 'X', '|', 's', '@', 'x', ' ', 'T', 'U', 'a', 'v', 'x', 'r', 'j', 'B', 'e', 'l', 'O', ' ', 'A', 'q', 'g', '-', 'B', 'o', 'y', 'D', 'o', 'A', 'S', 'd', 't', 'e']
every_third = list[::3]
print(every_third)

#reverses the order of the list
def Reverse_List(list):
    reversed_list = list[::-1]
    print(reversed_list)

#removes the ends of the list
sandwich_list = ["Bread", "Lettuce", "Tomato", "Cheese", "Ham", "Bread"]
glutanfree_sandwich = sandwich_list[1:-1]
print(glutanfree_sandwich)
