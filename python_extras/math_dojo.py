class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.num = num
        for a in nums:
            self.num = self.num + a
            self.result = self.num
            print(num, nums, self.result)
        return self

    def subtract(self, num, *nums):
        self.num = num
        for i in nums:
            self.num = self.num - i
            self.result = self.num
            print (num, nums, self.result)
        return self
# create an instance:

dojo_total = MathDojo()

dojo_total.add(3).add(4,7,9).subtract(4,6).result

md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
