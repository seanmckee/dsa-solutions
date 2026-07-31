class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for i, num in enumerate(nums):
            if count == 0:
                res = nums[i]
            if num == res:
                count += 1
            else:
                count -= 1
        return res

        