class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        majoritySize = len(nums)//2
        for key, val in count.items():
            if val >= majoritySize:
                return key

        