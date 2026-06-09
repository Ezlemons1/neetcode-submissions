import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            result = math.prod(rest)
            results.append(result)
        return results