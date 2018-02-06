students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def key_value(lst):
    for key in lst:
        print key['first_name'], key['last_name']

key_value(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def part_two(lst):
    for key in lst:
        counter = 0
        print key
        for j in lst[key]:
            counter += 1
            first_name = j['first_name']
            last_name = j['last_name']
            length = len(first_name) + len(last_name)
            print "{} - {}{} - {}".format(counter, first_name, last_name, length) 
        
part_two(users)