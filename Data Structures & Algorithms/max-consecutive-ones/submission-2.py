class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        finalMax = 0
        for n in nums:
            if n == 1:
                currentMax+= 1
            else:
                currentMax = 0
            if currentMax > finalMax:
                finalMax = currentMax
        return finalMax
        