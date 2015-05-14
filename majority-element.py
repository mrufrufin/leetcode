class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        for elt in set(nums):
            if nums.count(elt) > len(nums)/2:
                return elt
        return None 
