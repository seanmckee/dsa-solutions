class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_1d = []
        for l in matrix:
            matrix_1d = matrix_1d + l
        
        l, r = 0, len(matrix_1d)-1

        while l <= r:
            m = (l + r)//2

            if target < matrix_1d[m]:
                r = m -1
            elif target > matrix_1d[m]:
                l = l + 1
            else:
                return True
        return False
        