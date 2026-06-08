class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        counter = 0
        for i in strs:
            ans = [i]
            alph = ''.join(sorted(i))
            skip = False
            for a in answer:
                if ''.join(sorted(a[0])) == alph:
                    a.append(i)
                    skip = True
            if skip == False:
                answer.append(ans)
        return answer
