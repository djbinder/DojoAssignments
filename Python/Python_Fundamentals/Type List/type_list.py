#input variables
x = ['magical unicorns',19,'hello',98.98,'world']
y = [2,3,1,7,4,12]
z = ['magical', 'unicorns']

def typeList(list):
    resultString = "String: "       #sets a variable called 'resultString'
    sum = 0     #sets a variable called 'sum' and sets to zero   
    ints = 0        #sets a variable called 'ints' and sets to zero
    strings = 0     #sets a variable called 'strings' and sets to zero
    for val in list:        #looks through the values in the list
        if isinstance(val, str):        #asks if the value in the list is a string. 
            strings += 1        #if the value is a string, increase the strings variable by 1
            resultString += val + " "       #if the value is a string, add the val to the string and add a space afterwards
        elif isinstance(val, int) or isinstance(val, float):        #if it is not a string, check if val is an integer or float(a decimal number)
            ints += 1       #if it is an integer, increase ints variable by 1
            sum += val      #if it is an integer add the integer to the sum variable
            
    if ints != 0 and strings !=0:       #if ints ends up greater than 0 and strings ends up greater than 0
        print ("The list you entered is of mixed type")     #print the statement
        print (resultString)        #print all string values added to resultString 
        print ("Sum: " + str(sum))      #print the word "Sum" and convers 'sum' to string so it can be printed

print typeList(x)