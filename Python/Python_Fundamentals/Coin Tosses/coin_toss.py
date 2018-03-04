import random 

count_heads = 0
count_tails = 0

for a in range(5000):
    b = random.randint(1,101)
    x = 2
    z = (b % x)
    if (z > 0):
        print "heads"
        print 'Attempt:', count_heads+count_tails, 'Throwing a coin...Its a head!...Got', count_heads, 'so far and', count_tails, 'so far'
        count_heads = count_heads + 1
    else:
        print "tails"
        print 'Attempt:', count_heads+count_tails, 'Throwing a coin...Its a tails!...Got', count_tails, 'so far and', count_heads, 'so far'
        count_tails = count_tails + 1