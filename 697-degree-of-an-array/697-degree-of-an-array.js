/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function(nums) {
    
    let left = {}
    let right = {}
    let count = {}
    
    for(let i = 0; i < nums.length; i++){
        
        if (left.hasOwnProperty([nums[i]])){
            
        }else{
            left[nums[i]] = i
            
        }
        right[nums[i]] = i
        
        if (count.hasOwnProperty([nums[i]])){
            count[nums[i]]++
            
        }else{
            count[nums[i]] = 1
            
        }
        
    }
    
    let deg_array = []
    for (let key in count){
        
        deg_array.push(count[key])
    }
    
    
    let res = nums.length
    
    let degree = Math.max(...deg_array)
    
    
    for(let key in count){
        
        if (count[key] === degree){
            res = Math.min(res, right[key] - left[key] + 1)
        }
    }
    
    return res
    
    
    
};