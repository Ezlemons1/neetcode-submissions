class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = {}
        for str in strs:
            sortedstr = "".join(sorted(str))
            if sortedstr not in main:
                main[sortedstr] = [str]
            else:
                main[sortedstr].append(str)
        
        return list(main.values())