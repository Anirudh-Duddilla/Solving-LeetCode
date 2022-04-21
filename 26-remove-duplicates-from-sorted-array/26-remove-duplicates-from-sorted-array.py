class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, length = 0, len(nums)  #intitialize the starting index and the length of the list
        while start < length: #loop start with the condition that the index should always be less than length of the list
            #print(start,length)
            count = nums.count(nums[start]) # counting the occureneces of an element in the list
            #print(start,count,length)
            #print(nums)
            if count > 1: #if there are repeated elements then we are taking of the elements starting from to the ending point but not the ending one
                del nums[start+1: start+count]
            start = start+1 # incrementing one step hoping the next element is a new one
            length = length - count +1 #decreasing the length with reated elements-1 