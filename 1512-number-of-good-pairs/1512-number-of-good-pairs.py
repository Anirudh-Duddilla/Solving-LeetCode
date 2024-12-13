class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numsdict = defaultdict(list)
        res = 0
        for i, n in enumerate(nums):
            if numsdict[n] != [] and len(numsdict[n]) > 0:
                # print(numsdict[n])
                res += len(numsdict[n])
            numsdict[n].append(i)
            
        # print(numsdict)
        # print(res)
        
        return res