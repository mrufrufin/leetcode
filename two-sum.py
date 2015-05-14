class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        idx1 = None
        idx2 = None
        if target >= 0:
            numSort = filter(lambda x: x <= target, sorted(nums, reverse = True))
        else:
            numSort = filter(lambda x: x > target, sorted(nums))
        for cand in numSort:
            if target-cand in nums:
                idx1 = nums.index(cand) + 1
                idx2 = [i for i, n in enumerate(nums) if n == target-cand and i != idx1 - 1][0] + 1
                break
        if idx1 > idx2:
            temp = idx1
            idx1 = idx2
            idx2 = temp
        return [idx1, idx2]
        
