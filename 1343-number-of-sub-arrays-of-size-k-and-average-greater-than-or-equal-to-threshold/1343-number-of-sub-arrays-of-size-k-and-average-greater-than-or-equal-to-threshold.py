class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        sm = 0
        res = 0
        while r < len(arr):
            if (r-l) < k:
                sm += arr[r]
                r += 1
                if sm/k >= threshold and (r - l) == k:
                    # print("l", l,arr[l],"r", r,arr[r],"s", sm,"a", sm/k, sm/k >= threshold)
                    res += 1
                continue
            sm -= arr[l]
            l += 1
            
        return res