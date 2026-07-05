class Solution(object):
    def missingNumber(self, nums):

       num = set(nums)
       for i in range(len(nums) + 1):
          if i not in num:
            return i
