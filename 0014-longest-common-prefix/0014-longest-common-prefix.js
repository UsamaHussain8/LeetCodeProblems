/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let res = "";
    if (strs.length == 0)
        return res;

    let min_length = 1000000;    
    for (let idx = 0; idx < strs.length; ++idx) {
        if (min_length > strs[idx].length)
            min_length = strs[idx].length;
    }    
    
    for (let idx = 0; idx < strs[0].length; ++idx) {
        for (let num_elem = 1; num_elem < strs.length; ++num_elem) {
            if (strs[0][idx] != strs[num_elem][idx] || idx == strs[num_elem].length) {      
                console.log("I went in!")      
                return strs[0].substring(0, idx);
            }            
        }        
    }

    return strs[0];
};