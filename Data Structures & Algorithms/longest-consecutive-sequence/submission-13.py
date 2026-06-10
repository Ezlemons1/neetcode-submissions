class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)
        i = 0
        max_sequence = 1
        start_sequence = 0
        end_sequence = 0
        sequence = False

        if len(nums) == 0:
            return 0

        while i < len(nums)-1:
            if nums[i+1] - nums[i] == 1:
                if sequence == False:
                    sequence = True
                    start_sequence = i
                
                if i+1 == len(nums) - 1:
                    sequence_length = i+1 - start_sequence + 1
                    if sequence_length > max_sequence:
                        max_sequence = sequence_length
            elif nums[i+1] - nums[i] != 1:
                if sequence == True:
                    sequence = False
                    end_sequence = i
                    sequence_length = end_sequence - start_sequence + 1
                    if sequence_length > max_sequence:
                        max_sequence = sequence_length
            i += 1
        return max_sequence