class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #strin = set(s1) & set(s2)
        #if len(strin) == len(s1):
        #    return True
        #else:
        #    return False

        l = 0
        strlist = []
        for r in range(len(s2)):
            if r < len(s1) - 1:
                strlist.append(s2[r])
                continue
            strlist.append(s2[r])
            sub = "".join(strlist)
 
 
            if Counter(sub) == Counter(s1):
                return True
            else:
                l += 1
                strlist.pop(0)
        return False