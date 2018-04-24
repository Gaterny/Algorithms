# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twosum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                return [dict[num], i]
            else:
                dict[target-num] = i
