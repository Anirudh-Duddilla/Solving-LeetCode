class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res =[]

        ptr = 0

        while ptr < len(intervals) and intervals[ptr][1] < newInterval[0]:
            res.append(intervals[ptr])
            ptr += 1

        while ptr < len(intervals) and (intervals[ptr][0] <= newInterval[1]):
            newInterval[0] = min(intervals[ptr][0], newInterval[0])
            newInterval[1] = max(intervals[ptr][1], newInterval[1])
            ptr+=1
        res.append(newInterval)

        while ptr < len(intervals):
            res.append(intervals[ptr])
            ptr+=1

        return res