import random
import numpy as  np
# Shuffle
# In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?

def shuffle(arr, num):
    # Start from the last index and swap each one
    for x in range(num-1,0,1):
        i = random.randint(0, x + 1)
        arr[x], arr[i] = arr[i], arr[x]
    return arr

arr = np.array([2,4,90,23,10])

num = len(arr)
print(shuffle(arr, num))

# Skyline Heights
# Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().

def skylines(arr):
    new_arr = []
    building = 0
    for i in arr:
        if i > building and i >= 0:
            building = i
            new_arr.append(i)
    return new_arr

print(skylines([-1,1,1,7,3]))

# Zip It
# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].

arr_1 = [4,5,100]
arr_2 = [10,20,30,40]

print ("The first array is:" + str(arr_1))
print ("The second array is : " + str(arr_2))

size_arr_1 = len(arr_1)
size_arr_2 = len(arr_2)

merge = []
i, j = 0, 0

while i < size_arr_1 and j < size_arr_2:
    if arr_1[i] < arr_2[j]:
        merge.append(arr_1[i])
        i += 1

    else:
        merge.append(arr_2[j])
        j += 1

merge = merge + arr_1[i:] + arr_2[j:]
print ("The combined sorted array is : " + str(merge))
