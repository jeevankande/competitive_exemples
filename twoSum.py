


import random

class Solution:
    def twoSum(self,nums,target):
        """Error without self TypeError: twoSum() takes 2 positional arguments but 3 were given"""
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i



a = Solution()
l=[11, 10, 12, 27, 29]
#l = random.sample(range(10, 30), 5) 
print(l)
print(a.twoSum(l,21))