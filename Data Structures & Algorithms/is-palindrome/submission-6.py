class Solution:
    def isPalindrome(self, s: str) -> bool:
        # normalize the string
        s = s.lower()
        s = [s[i] for i in range(len(s)) if s[i].isalnum()]
        "".join(s)
        start = 0
        end = len(s) - 1
        while start != end and start < end:
            print(s[start])
            print(s[end])
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True