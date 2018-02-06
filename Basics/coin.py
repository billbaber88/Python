

def coin_flip(throws):
    headcount = 0
    tailcount = 0
    for i in range (1, (throws)+1):
        import random
        flip = random.randint(0, 1)
        print flip
        if flip is 1:
            headcount +=1
            print "Attempt #", i, ": Throwing a coin... it's heads! You have gotten heads ", headcount, " so far, and tails ", tailcount, " so far. ", (5000-i), " throws to go!"
        else:
            tailcount +=1
            print "Attempt #", i, ": Throwing a coin... it's tails! You have gotten heads ", headcount, " so far, and tails ", tailcount, " so far. ", (5000-i), " throws to go!"


coin_flip(50)