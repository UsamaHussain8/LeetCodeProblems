/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    let num_zeros = 0;
    let cur_zeros = 0;

    for (let idx = 0; idx <= nums.length - 1; idx++) 
    {
        if (nums[idx] === 0) 
        {
            cur_zeros += 1;
            num_zeros += cur_zeros;
        }
        else 
            cur_zeros = 0;
    }
        return num_zeros; 
}