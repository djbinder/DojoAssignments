
#TYPES
print type (45)
print type ("Dan")
print type ([1, 3, 4])

#LEN | LENGTH
print len(["item1","item2","item3"]) #returns 3
print len("this is a sentence to count the characters") #returns 42
parrot = "Norwegian Blue" #sets variable
    len(parrot)                      #gets the length of the variable
    print len(parrot)              #print the length of the variable

#LOWER
"Ryan".lower() #returns "ryan"

# FOR loops - demo1
for count in range(0, 5):
    print "looping - ", count

# FOR loops - demo2
my_list = [4, 'dog', 99, ['list','inside','another'], 'hello world!']
for element in my_list:
    print element

# FOR loops - demo3
for i, v in enumerate (['tic', 'tac', 'toe']):
    print i, v

# WHILE loops - demo1
count = 0
while count < 5: 
        print 'looping -', count
        count += 1

# SUM LIST
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))

# AVERAGE LIST
def average_list(items):
    average_numbers = 0
    for x in items:
        average_numbers += x
    return average_numbers / count
print(average_list([1,2,3,4,5]))

#IF ELSE NESTED 
x = "Dan is a name that has letters in it like this sentence does" #note: change this to any of a string, integer or array
if isinstance(x, int):
    if(x >= 100): 
        print("big number")
    else:
        print("small number")
if isinstance(x, str):
    if (len(x) >=50):
        print("long sentence")
    else:
        print("short sentence")
if isinstance(x, list):
    if(len(x) >= 10):
        print("big list")
    else:
        print("short list")