class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = {}
        tlist = {}
        for i in s:
            if i not in slist:
                slist[i] = 1
            else:
                slist[i] += 1
        
        for j in t:
            if j not in tlist:
                tlist[j] = 1
            else:
                tlist[j] += 1

        if slist == tlist:
            return True
        else:
            return False