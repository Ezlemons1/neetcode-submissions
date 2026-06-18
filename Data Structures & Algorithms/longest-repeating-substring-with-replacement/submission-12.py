class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        length = 0
        for j in range(len(s)):
            sub = s[i:j+1]
            print(sub)
            sdict = Counter(sub)
            freq = sdict.most_common(1)[0][1]
            print("freq = " + str(freq))
            if (j-i + 1) - freq > k:
                i += 1
                print('^ did not pass')
            else:
                length = max(length, j-i + 1)
        return length