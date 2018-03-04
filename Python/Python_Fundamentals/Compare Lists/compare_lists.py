list_one = [2,2,5,6,2]
list_two = [1,2,5,6,2]
list_three = [1,2,3,4,5]
list_four = [1,2,3,4,5]

def complist(list1, list2):
    matches = 0
    i = 0
    stop = len(list1)
    while i < stop:
        if list1[i] == list2[i]: 
            i +=1
            matches += 1
        else:
            print "the lists do not match"
            break
    if stop == matches:
        print "the lists match"

complist(list_three, list_four)