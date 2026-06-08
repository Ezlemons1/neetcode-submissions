class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        area = 0
        temp = [0]

        def dfs(row,col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return
            grid[row][col] = 0
            temp[0] += 1
            for r,c in directions:
                dfs(row+r,col+c)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row,col)
                    if temp[0] > area:
                        area = temp[0]
                    temp[0] = 0
        
        return area
                