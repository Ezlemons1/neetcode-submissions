class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = defaultdict(list)
        for str in strs:
            sortedstr = "".join(sorted(str))
            main[sortedstr].append(str)
        
        return list(main.values())