/**
 * @param {number} n
 * @param {number[]} rounds
 * @return {number[]}
 */
var mostVisited = function(n, rounds) {
    let first = rounds[0]
    let last = rounds[rounds.length -1]
    let res = []
    if (first <= last){
        for(let i = first; i < last+1; i++){
            res.push(i)
        }
        
    } else{
        
        for (let i = 0; i<n; i++){
            if (i + 1 <= last || i+1 >= first){
                res.push(i+1)
            }
        }
    }
    return res
};