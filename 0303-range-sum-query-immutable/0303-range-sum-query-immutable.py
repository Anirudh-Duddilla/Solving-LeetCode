class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        while left <= right:
            # print(left,self.nums_array[left],right,self.nums_array[right],sum)
            if left == right:
                sum = sum + self.nums_array[left]
                return sum
            sum = sum + self.nums_array[left] + self.nums_array[right]
            left += 1
            right -= 1
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)