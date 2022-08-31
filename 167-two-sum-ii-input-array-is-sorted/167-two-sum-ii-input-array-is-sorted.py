class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        
        while l < r:
            two_some = numbers[l] + numbers[r]
            
            if two_some > target:
                r -= 1
            elif two_some < target:
                l += 1
            
            else:
                return [l+1,r+1]
            