class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(numbers):
            pairs[num] = { "index": i, "used": False}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in pairs and not pairs[complement]["used"] and pairs[complement]["index"] != i:
                return [min(i, pairs[complement]["index"])+1,max(i, pairs[complement]["index"])+1]