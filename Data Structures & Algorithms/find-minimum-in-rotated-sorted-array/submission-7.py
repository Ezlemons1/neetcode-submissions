class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = 1001
        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])

            if nums[mid] < minimum:
                minimum = nums[mid]

            if nums[right] > nums[mid] > nums[left]:
                return nums[left]
            elif nums[mid] >= nums[left]:# and nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[left]:# and nums[mid] < nums[right]:
                right = mid - 1

        return minimum