# 1. Countdown
# Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?

# def countdown(num):
#     arr=[]
#     for i in range(num,-1,-1):
#         arr.append(i)
#     return arr

# print(countdown(10))

# 2. First Plus Length
# Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

# arr = [2,6,8,9]
# print(arr[0] + len(arr))
# Output is 6

# arr = ["yes",8,15,12]
# print(arr[0] + len(arr))
# Output
# TypeError: can only concatenate str (not "int") to str

# arr = [False,8,15,12]
# print(arr[0] + len(arr))
# Output would be 4 , if True was on the index 0 then ouput would be 5

# 3. Values Greater than Second
# For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

# def greater_than_second(arr):
#     times= 0
#     for i in arr:
#         if i > arr[1]:
#             print(i)
#             times += 1
#             print(f'{times} times greater than its second value')
#     return arr

# print(greater_than_second([10,5,20,23,18]))

arr = [42,68,7,21,243,512]
for  x in len(arr)-2:
    if (x > 1):
        arr[x - 1] = arr[x + 1]
print(arr)
print(x)