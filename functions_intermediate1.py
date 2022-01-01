# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1-1
print(x)
x[1][0] = 15
print(x)
# 1-2
students[0]['last_name'] = 'Bryant'
print(students)
# 1-3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# 1-4
z[0]['y'] = 30
print(z)

# 2. Iterate through a list of Dictionaries
students_two = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    string = ''
    for val in some_list:
        string += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
        return string
print(iterateDictionary(students_two))

# 3.Get Values froma list of Dictionaries
def iterateDictionary2(key_name, some_list):
    string = ''
    for val in some_list:
        string += f"{val[key_name]}\n"
    return string
print(iterateDictionary2('first_name' , students_two))

# 4. Iterate with a dictionary through lists values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for val in some_dict:
            print(val)
print(printInfo(dojo))
