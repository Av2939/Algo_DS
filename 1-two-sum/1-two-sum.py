class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        
        for i in range(len(nums)):
            
            val = target - nums[i]
            
            if val in hashSet:
                return [hashSet[val], i]
            
            hashSet[nums[i]] = i
            
            