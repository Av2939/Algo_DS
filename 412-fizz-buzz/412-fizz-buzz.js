/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    
    let res = [];
    
    for (let i = 1; i< n + 1; i++){
        console.log(i)
        
        if (i % 5 === 0 && i % 3 === 0){
            res.push("FizzBuzz")
        } else if (i % 3 === 0){
            res.push("Fizz")
        } else if (i % 5 === 0){
            res.push("Buzz")
        } else {
            res.push(String(i));
        }
    }
    return res;
    
    
};