class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answerlist = []
        for r in range(k-1, len(nums)):
            # increments r, will have to increment l at every iteration
            sublist = nums[r-k+1:r+1]
            print(r-k+1)
            answerlist.append(max(sublist))
        return answerlist