class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = nums
        self.prefix = []
        pre_sum = 0
        for n in self.nums_array:
            pre_sum += n
            self.prefix.append(pre_sum)
            
    def sumRange(self, left: int, right: int) -> int:
        # sum = 0
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)