mixedBag = ['unicorns',19,'hello',98.98,'world']
nums = [1, 2, 3, 4, 5, 123323, -123, 1332, -12323, 8]
werds = ['hello', 'is', 'it', 'me', 'you\'re', 'looking', 'for']

def checkList(lst):
    total = 0
    newStr = ''
    for x in lst:
        if isinstance(x, float) or isinstance(x, int):
            total += x
        elif isinstance(x, str):
            newStr += x
    
    if total and newStr:
        print "The array you entered is of the mixed type"
        print "String: ", newStr
        print "total: ", total
    elif newStr:
        print "It's a striiiiiiing!"
        print "String: ", newStr
    else:
        print "All numbers, homie"
        print "total: ", total

print checkList(mixedBag)
print checkList(nums)
print checkList(werds)
