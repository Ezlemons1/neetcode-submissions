class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            goal = target - nums[i]
            temp = nums
            temp[i] = -999
            if goal in temp:
                j = temp.index(goal)
                break
        return [i, j]