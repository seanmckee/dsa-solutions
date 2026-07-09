class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in numDict:
                return sorted([i, numDict[complement]])
            numDict[num] = i
