class NumArray:

    def __init__(self, nums: List[int]):
        self.numsArray = nums
        self.length = len(self.numsArray)

    def sumRange(self, left: int, right: int) -> int:
        cum_sum: int = 0
        for i in range(left, right + 1):
            cum_sum += self.numsArray[i]
            if i >= self.length:
                break

        return cum_sum
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)