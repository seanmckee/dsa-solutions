class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, i = 0, len(nums)-1, 0

        def swap(a , b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
            else:
                i += 1