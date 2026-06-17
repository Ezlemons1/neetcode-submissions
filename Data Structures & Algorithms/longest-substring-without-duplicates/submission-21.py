class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 1
        i = 0
        j = i
        tempdict = {}
        templength = 0
        if not s:
            return 0

        while i < len(s) - 1:
            print(j)
            if s[j] not in tempdict.keys():
                print(True)
                tempdict[s[j]] = s[j]
                templength += 1
                
                # increment protocol
                if j == len(s) - 1:
                    i += 1
                    j = i
                else:
                    j += 1

            else:
                print(False)
                if templength > maxlength:
                    maxlength = templength
                tempdict = {}
                templength = 0
                i += 1
                j = i

        if templength > maxlength:
            maxlength = templength

        return maxlength