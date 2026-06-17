class Solution:
    def trap(self, height: List[int]) -> int:
        totalarea = 0
        l = 0
        r = len(height) - 1
        prefixmax = []
        suffixmax = []
        currpmax = 0
        currsmax = 0
        
        while l != len(height) and r != -1:
            temppmax = height[l]
            tempsmax = height[r]
            if temppmax > currpmax:
                currpmax = temppmax
            if tempsmax > currsmax:
                currsmax = tempsmax
            prefixmax.append(currpmax)
            suffixmax.append(currsmax)
            l += 1
            r -= 1
        
        print("prefixmax: " + str(prefixmax))
        print("suffixmax: " + str(suffixmax))
        print("heights: " + str(height))

        suffixmax.reverse()
        for i in range(len(prefixmax)):
            area = min(prefixmax[i], suffixmax[i]) - height[i]
            totalarea += area
        
        return totalarea