class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = 0
        for i in nums:
            counter += 1
            for j in range(counter, len(nums)):
                if i == nums[j]:
                    return True
        return False
         