bill = {
    'name': 'Bill',
    'age': 29,
    'location': 'Chicago',
    'favorite language': 'English',
}

taco = {
    'name': 'Taco',
    'age': 4.5,
    'location': 'Bill\'s Apartment',
    'favorite language': 'Meow',
}

potus = {
    'name': 'Trump',
    'age': '70ish',
    'location': 'Washington, DC',
    'favorite language': 'Doublespeak',
}


def tell_me_about(lst):
    first = ''
    value = ''
    for key,data in lst.iteritems():
        first = key
        value = data
        print 'His',first,"is",value,"." 

def dif_tell_me_about(lst):
    for i in lst:
        print 'His',i,"is",lst[i],"."


tell_me_about(bill)
tell_me_about(taco)
tell_me_about(potus)

dif_tell_me_about(bill)
dif_tell_me_about(taco)
dif_tell_me_about(potus)

