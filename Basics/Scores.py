import random

random_num = random.randint(60, 100)
print random_num

def grades_reaction(num):
    if random_num < 70:
        print "Grounded. No more fun until your grades are up"
    elif random_num >= 70 and random_num < 80:
        print "That's a C. Try a little harder next time"
    elif random_num >= 80 and random_num < 90:
        print "Bees?!"
    else:
        print "This is the first time I've ever been proud of you."


grades_reaction(random_num)