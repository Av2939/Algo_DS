class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = collections.defaultdict(list)
        
        for s in strs:
            dict[str(sorted(s))].append(s)
        
        return dict.values()