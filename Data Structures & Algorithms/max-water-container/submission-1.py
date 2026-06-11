class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        i = 0
        j = 1
        while i < len(heights) - 1:
            x = j - i
            area = x * min(heights[i], heights[j])
            if maxarea < area:
                maxarea = area
            
            if j == len(heights) - 1:
                i += 1
                j = i + 1
            else:
                j += 1

        return maxarea