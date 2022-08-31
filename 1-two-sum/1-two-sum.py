class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Dict = {}
        
        for i in range(len(nums)):
            
            val = target - nums[i]
            
            if val in Dict:
                return[Dict[val], i]
            
            Dict[nums[i]] = i