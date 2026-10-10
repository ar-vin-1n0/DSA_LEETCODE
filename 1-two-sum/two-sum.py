class Solution(object):
        def twoSum(self, nums, target):
            hash = {}

            for i in range(len(nums)):
                result = target - nums[i]
                if result in hash:
                    return [i,hash[result]]
                hash[nums[i]] = i    




        