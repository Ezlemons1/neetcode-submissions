class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        length = 0
        sdict = {}
        freq = 0
        for j in range(len(s)):
            sdict[s[j]] = sdict.get(s[j], 0) + 1
            freq = max(freq, sdict[s[j]])
            print("freq = " + str(freq))
            if (j-i + 1) - freq > k:
                sdict[s[i]] -= 1
                i += 1
                
                print('^ did not pass')
            else:
                length = max(length, j-i + 1)
        return length