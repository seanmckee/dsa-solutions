class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        print(frequency)
        for key, val in frequency.items():
            print(val)
            if val > 1:
                return True
        return False