x = "Dan is a name that has letters in it like this sentence does"
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