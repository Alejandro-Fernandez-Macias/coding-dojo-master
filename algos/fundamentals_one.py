# 1. Multiples of Three – but Not All
# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

for i in range(-300,0,3):
    if i == -6:
        break
    print(i)

# 2. Printing Integers with While
# Print integers from 2000 to 5280, using a WHILE.

# num = 2000
# while num <= 5280:
#     print(num)
#     num= num + 1

# 3. Counting, the Dojo Way
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

# for i in range(1,100):
#     if i % 5 == 0:
#         print("Coding")
#     if i % 10 == 0:
#         print("Dojo")
#     else:
#         print(i)

# 4. Flexible Countdown
# Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

# nums=[2, 9, 3]
# high_num = []
# for i in nums:
#     if ( i > ):
#         high_num.append(i)
#         print("high_num", high_num)