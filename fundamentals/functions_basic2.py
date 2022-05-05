# 1.countdown
def countdown(n):
    nlist = []
    for x in range(n, -1, -1):
        nlist.append(x)
    return nlist
print(countdown(40))

# 2. Print and reurn
def print_and_return(newlist):
    print(newlist[0])
    return newlist[1]
print(print_and_return([10, 50]))

# 3. First Plus Length
def first_plus_length(newlist):
    sum = newlist[0] + len(newlist)
    print(newlist[0])
    print(len(newlist))
    return sum
print(first_plus_length([1,2,3,4,5,6,7,8,9]))

# 4. Values greater than second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    newlist = []
    for num in list:
        if num > list[1]:
            newlist.append(num)
    print(len(newlist))
    return newlist
print(values_greater_than_second([5,2,3,2,1,9,7]))
print(values_greater_than_second([5,4,3,2,1,9,7]))
print(values_greater_than_second([2]))

# 5. This Length, This Value
def length_and_value(size, value):
    newlist = []
    for x in range(size):
        newlist.append(value)
    return newlist
print(length_and_value(5,10))



