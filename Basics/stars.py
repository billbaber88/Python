def draw_stars(lst):
    for x in lst:
        print '*'*x


nums = [3, 9, 3, 11, 5, 6, 1, 8, 2, 10]

draw_stars(nums)

def part_two(lst):
    for y in lst:
        if isinstance(y, str): 
            print y[0]*len(y)
        else:
            print "*"*y
    
    print lst

my_list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

part_two(my_list)