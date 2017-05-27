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

def printUsers(arr):
    for key, data in arr.items():
        print key
        # print data
        index = 1
        for value in data:
            # print value
            # index = data.index("value")
            # print index
            name_len = len(value["first_name"]) + len(value["last_name"])
            print index, "-", value["first_name"], value["last_name"], "-", name_len
            index += 1


printUsers(users)
