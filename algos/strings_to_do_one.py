# Challenge: what is displayed by the following? Why?
# print(1 + 2 + "3" + "4" + 5 + 6)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Strings To Do 1
# Remove Blanks
# Create a function that, given a string, returns all of that string’s contents, but without blanks.
# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

def unite(string):
    print(string)
    return string.replace(" ", "")

# new_string = unite("Pl ayTha tF u nkyM usic")
# print(f'New string after removing the blanks: {new_string}')

# Get Digits
# Create a function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.

def get_digits(obj):
    string =obj.split(" ")
    num = ""
    x=0
    for x in range(x < len(string),1):
        if(string[x] % 1 == 0):
            num += string[x]
    return num / 1

# print(get_digits('0s1a3y5w7h9a2t4?6!8?0'))

# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
# Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW".
# Given "Live from New York, it's Saturday Night!", return "LFNYISN".

def get_acronym(string):
    string_arr = string.split(" ")
    acry = ""
    idx = 0
    for idx in range (len(string_arr)):
        if (string_arr[idx] == False):
            continue
        else:
            acry += string_arr[idx][0].upper()
            print(acry)
    return acry

# print(get_acronym("Live from New York, it's Saturday Night!"))

# Zip Arrays into Map
# Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

# Example 1:
arr_1 = ['abc', 3, 'yo']
arr_2 = [42, 'wassup', True]
assoc_arr = {arr_1[0]: arr_2[0], arr_1[1]:arr_2[1], arr_1[2]: arr_2[2]}
print(assoc_arr)

# Example 2:
assoc_arr = {}
assoc_arr['abc'] = 42
print(assoc_arr)
assoc_arr[3] = 'wassup'
print(assoc_arr)
assoc_arr['yo'] = True
print(assoc_arr)

# Invert Hash
# Associative arrays are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys.
# Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

def invert_hash(assoc_arr):
    assoc_arr = {v: k for k, v in assoc_arr.items()}
    return assoc_arr

print(invert_hash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))