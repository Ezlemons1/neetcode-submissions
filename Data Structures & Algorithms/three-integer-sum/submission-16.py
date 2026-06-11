class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = nums[i] + nums[j] + nums[k]
                if result == 0 and [nums[i], nums[j], nums[k]] not in results:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif result < 0:
                    j += 1
                else:
                    k -= 1
              
        return results