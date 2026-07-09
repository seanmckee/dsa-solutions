class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped_nums = {}
        for i, num in enumerate(nums):
            mapped_nums[num] = i
        for i, num in enumerate(nums):
            pair = target - num
            if pair in mapped_nums and mapped_nums[pair] != i:
                return [i, mapped_nums[pair]]
        
              