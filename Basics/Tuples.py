my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tup(lst):
    new_list = []
    for k,v in lst.iteritems():
        new_list.append((k,v))
    print new_list


tup(my_dict)

