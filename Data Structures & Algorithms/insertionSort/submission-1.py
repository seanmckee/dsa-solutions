# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        outputList = [pairs.copy()]
   
        for i in range(1, len(pairs)):
            j = i - 1
            current = pairs[i]
            while j >= 0 and current.key < pairs[j].key:
                pairs[j+1] = pairs[j]
                pairs[j] = current
                j -= 1
            outputList.append(pairs.copy())
        return outputList