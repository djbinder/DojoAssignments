def draw_stars(star_list):
    for i in star_list:
        if isinstance(i, int):
            print ('*' * i)
        if isinstance(i, str):
            print (i.lower()[:1] * len(i))


star_list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(star_list)





