class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numList = {}
        for i, num in enumerate(nums):
            if num in numList.values():
                return True
            numList[i] = num
        return False
            
        
        