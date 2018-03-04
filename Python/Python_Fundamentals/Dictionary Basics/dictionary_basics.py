def about_me(dictionary):
    print 'My name is', dictionary["Name"]
    print 'My age is', dictionary["Age"]
    print 'My country of birth is the', dictionary["Born"]
    print 'My favorite language is', dictionary["Language"]

dictionary = {"Name" : "Dan", "Age" : "34", "Born" : "USA", "Language" : "Python"}
about_me(dictionary)
