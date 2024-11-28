class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left,right+1):
            # print(i,self.nums_array[i])
            sum += self.nums_array[i]
            
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)