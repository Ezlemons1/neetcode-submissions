class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(numbers):
            # check if the two current nums sum to target
            if numbers[i] + numbers[j] == target:
                break
            if j == len(numbers) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        return [i+1, j+1]