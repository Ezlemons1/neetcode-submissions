class Solution:
    def isValid(self, s: str) -> bool:
        chardict = {')':'(', ']':'[', '}':'{'}
        q = deque()
        if len(s) % 2 == 1:
            return False
        for st in s:
            
            if st in chardict.keys():
                if not q:
                    return False
                if q and q[-1] != chardict[st]:
                    return False
                q.pop()
            else:
                q.append(st)
            print(q)
        if q:
            return False
        else:
            return True
