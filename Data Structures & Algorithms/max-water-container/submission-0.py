class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMax = 0
        p1, p2 = 0, len(heights)-1

        while(p1 < p2):
            currentArea = min(heights[p1], heights[p2])* (p2-p1)
            if currentArea > currentMax: 
                currentMax = currentArea
            if(heights[p1] < heights[p2]):
                p1 += 1
            else:
                p2 -= 1
        return currentMax