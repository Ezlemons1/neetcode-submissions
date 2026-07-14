class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 is smallest array always
        if len(nums2) <= len(nums1):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:

            # partition markers for nums1 and nums2 respectively
            mid1 = (left + right) // 2
            mid2 = half - mid1

            # find values left and right of partitions
            if mid1 == 0:
                left1 = float('-inf')
            else:
                left1 = nums1[mid1 - 1]
            
            if mid2 == 0:
                left2 = float('-inf')
            else:
                left2 = nums2[mid2 - 1]
            
            if mid1 == m:
                right1 = float('inf')
            else:
                right1 = nums1[mid1]
            
            if mid2 == n:
                right2 = float('inf')
            else:
                right2 = nums2[mid2]
            
            # if partition is valid
            if left1 <= right2 and left2 <= right1:
                print('yes')
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return float(max(left1, left2))
            elif left1 > right2:
                print('no')
                right = mid1 - 1
            else:
                print('no')
                left = mid1 + 1
        
        return -1.0
