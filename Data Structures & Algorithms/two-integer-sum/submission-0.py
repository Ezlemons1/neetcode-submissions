class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = 1
        answer = []
        for i in nums:
            for j in range(counter, len(nums)):
                if i + nums[j] == target:
                    answer.append(counter-1)
                    answer.append(j)
                    break
            counter += 1
        return answer