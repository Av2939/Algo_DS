class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        
        for i in range(len(nums)):
            
            res = target - nums[i]
            
            if res in hashSet:
                return [hashSet[res], i]
            
            hashSet[nums[i]] = i
            