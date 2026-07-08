class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bot = row - 1
        
        answer = False
        
        while top <= bot:
            midrow = (top + bot) // 2
            left = 0
            right = col - 1
            while left <= right:
                midcol = (left + right) // 2
                if matrix[midrow][midcol] == target:
                    return True
                elif matrix[midrow][midcol] > target:
                    right = midcol - 1
                elif matrix[midrow][midcol] < target:
                    left = midcol + 1
            if matrix[midrow][midcol] > target:
                bot = midrow - 1
            elif matrix[midrow][midcol] < target:
                top = midrow + 1
        
        return answer
                
                    