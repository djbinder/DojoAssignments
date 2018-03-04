def return_names(bulls):
    for i in bulls:
        print(i)["First"] + " " + (i)["Last"]
        
bulls = [{"First" : "Michael", "Last" : "Jordan"}, {"First" : "Scottie", "Last" : "Pippen"}, {"First" : "Dennis", "Last" : "Rodman"}, {"First" : "Toni", "Last" : "Kukoc"}]
return_names(bulls)

def final_list(main_lists):
    count = 1
    for title, names in main_lists.iteritems():
        for values in names:
            print count, values["First"] + " " + values["Last"]
            count = count + 1

main_lists = {
    'bulls': [
        {"First" : "Michael", "Last" : "Jordan"}, 
        {"First" : "Scottie", "Last" : "Pippen"}, 
        {"First" : "Dennis", "Last" : "Rodman"}, 
        {"First" : "Toni", "Last" : "Kukoc"}
    ], 
    'Instructors': [
        {"First" : "Phil", "Last" : "Jackson"},
        {"First" : "Fred", "Last" : "Hoiberg"}
    ]
}

final_list(main_lists)