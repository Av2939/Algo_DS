class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums)-1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total< target:
                    result += (k-j)
                    j += 1
                else:
                    k -= 1
        return result