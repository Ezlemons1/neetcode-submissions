class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = Counter(t)
        count2 = {}
        have = 0
        need = len(count1)
        answer = ""
        l = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            sub = s[l:r]
            print(sub)
            count2[s[r]] = count2.get(s[r], 0) + 1
            
            if s[r] in count1 and count2[s[r]] == count1[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                count2[s[l]] -= 1
                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""




