# input
word_list = ['oval','my','name','is','Anna','orange']
char = 'o'
# output
new_list = ['hello','world']


def find_characters(list, letter):      #create function. make it require a list and a character
    n=[]        #establish 'n' as a blank list
    for item in list:       #looks through each item in the list
        print item.find(letter)
        if item.find(letter) != -1:     #looks through each item in the list and checks for the letter
            n.append(item)      #if the above found the letter in the last, append the item to n (i.e., the blank list variable)
    print n     # once done cycling, print out the list


find_characters(word_list, char)