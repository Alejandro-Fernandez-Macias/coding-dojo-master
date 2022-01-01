# 1. Basic
for num in range(151):
    print(num)
    
# 2. Multiples of five
for x in range(5,1001,5):
    print(x)

# 3.Counting, the Dojo Way
for num1 in range(1,101):
    if (num1 % 5 == 0):
        print("Coding")
    if (num1 % 10 == 0):
        print("Coding Dojo")
    else: print(num1)

# 4. Whoa. That Sucker's Huge
sum = 0
for i in range(1,500000):
    if( i % 2 == 1):
        sum += i
        print(sum)

# 5. Countdown by fours
for nums in range(2018,0,-4):
    if (nums % 2 == 0):
        print(nums)

# 6. Flexible Counter
lownum = 2
highnum = 10
mult = 3
for numbers in range(lownum,highnum):
    if (numbers % mult == 0):
        print(numbers)
