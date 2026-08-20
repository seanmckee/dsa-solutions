class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        print(counts)

        j = 0
        colors = [0,1,2]
        for c in colors:
            for i in range(counts.get(c, 0)):
                nums[j] = c
                j = j+1
            