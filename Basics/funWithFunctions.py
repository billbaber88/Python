def oddOrEven():
    for i in range(1, 2001):
        if i%2 is 0:
            print "Number is ", i, ". This is an even number."
        else:
            print "Number is ", i, ". This is an odd number."

oddOrEven()

def times_num(arr, num):
    for i in range(0, len(arr)):
        arr[i] = arr[i]*num
    print arr
    return arr

my_list = [1, 2, 3, 4, 5, 6]

# times_five(my_list, 2)

def layered_multiples(arr):
    new_arr = []
    for i in range (0, len(arr)):
        new_arr.append("I"*arr[i])
    print new_arr

layered_multiples(times_num(my_list, 7))

