class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "-" + string
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        results = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "-":
                j += 1
            length = int(s[i:j])
            diff = j-i + 1
            print(length)
            print("".join(s[i+diff:i+length+diff]))
            results.append("".join(s[i+diff:i+length+diff]))
            i += length + diff
        return results