# Create a series of functions based on the below descriptions.

# Odd/Even:
    # Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

for count in range(1, 2001):
    x = 2
    y = count
    z = (y % x)
    if (z > 0):
        print "Number is %s. This is an odd number." %(y)
    else:
        print "Number is %s. This is an even number." %(y)

# Multiply:
    # Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(my_list, n):   
    my_new_list = [i * n for i in my_list]
    return(my_new_list)
print(multiply([2,4,10,16], 5))

# Hacker Challenge:
    # Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list.


def layered_multiples(arr):
    new_array = []
    for i in arr:
        print ('1' * i)
        new_array.append('1' * i)
    print new_array


arr = [6,2,3]
layered_multiples(arr)
