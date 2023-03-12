# Python Program to select Even items of a list


def even_item(a):
    b = []
    # check length of list
    if len(a) > 0:
        for num in a:
            if num % 2 == 0:
                b.append(num)
    
    print("Even items of a list is: ", b)

# create a list

# a = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for given input list

num = int(input("Enter number of List 1 integer items: "))
a = []

for i in range(0, num):
    c = int(input(f"Enter List 1 integer item {i}: "))
    a.append(c)

print("List is: ", a)

even_item(a)

# Thanks for Watching