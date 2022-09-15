/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const Sett = new Set()
    
    for (let i = 0; i < nums.length; i++){
        
        if (Sett.has(nums[i])){
            return true
        }
        Sett.add(nums[i])
        
        
    } 
    return false
    
};