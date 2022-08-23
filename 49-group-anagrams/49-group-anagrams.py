class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        Dict = collections.defaultdict(list)
        
        for s in strs:
            Dict[str(sorted(s))].append(s)
        
        return Dict.values()