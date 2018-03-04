#STRINGS AND LISTS
    
#FIND and REPLACE
    # string.find(s, sub[, start[, end]])
    # Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices.

# words = "It\'s thanksgiving day. It\'s my birthday,too!"
# print words.find("day")
# print words.replace("day", "month")


#MIN and MAX

# random_numbers = [2, 43, 17, -1, 29, 990]
# print max(random_numbers)
# print min(random_numbers)


# #FIRST and LAST
# rand_numbers = [13,16,"Dan",27,"Binder"]
# print rand_numbers[0]
# print rand_numbers[4]
# print rand_numbers[max(rand_numbers)]

#NEW LIST

x = [19,2,54,-2,7,12,98,32,10,-3,6] 
print sorted(x)
x_sorted = sorted(x)
print x_sorted[0:6]


