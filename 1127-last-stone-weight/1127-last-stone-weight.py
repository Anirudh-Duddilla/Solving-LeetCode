class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sheap = [-n for n in stones]
        diff = 0
        while len(sheap) > 1:
            heapq.heapify(sheap)
            # print("strt ",sheap)
            max1, max2 = heapq.nsmallest(2, sheap)
            # print("m1: ", max1, "m2: ", max2)
            
            if max2 > max1:
                diff = max1 - max2
            elif max2 == max1:
                diff = 0
            heapq.heappop(sheap)
            # print("am1: ", sheap)
            heapq.heappop(sheap)
            # print("am2: ", sheap)
            
            sheap.append(diff)

        return -sheap[0]
            
        