class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            temp[num] += 1
        for n, v in temp.items():
            buckets[v].append(n)

        results = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                results.append(j)
                if len(results) == k:
                    return results
        
        return results