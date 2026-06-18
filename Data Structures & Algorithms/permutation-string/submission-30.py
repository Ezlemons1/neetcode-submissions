class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        if count1 == count2: return True
        for r in range(len(s1), len(s2)):
            count2[s2[r]] += 1
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            if count1 == count2:
                return True
        return False