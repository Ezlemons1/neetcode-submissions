class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)
        answerk = max(piles) + 1
        while low <= high and high >= 2:
            k = (low + high) // 2
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / k)
            if count > h:
                low = (k + 1)
            elif count <= h and k < answerk:
                answerk = k
                high = (k - 1)
        
        return answerk