class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashlist = defaultdict(int)
        for num in nums:
            if hashlist[num]:
                return num
            else:
                hashlist[num] = 1
        
