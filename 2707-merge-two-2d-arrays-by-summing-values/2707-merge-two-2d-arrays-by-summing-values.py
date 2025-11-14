class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        f, s = 0, 0
        res = []

        while f < len(nums1) and s < len(nums2):
            if nums1[f][0] < nums2[s][0]:
                res.append(nums1[f])
                f += 1
            elif nums1[f][0] > nums2[s][0]:
                res.append(nums2[s])
                s += 1
            else:
                res.append([nums1[f][0], nums1[f][1]+nums2[s][1]])
                f+=1
                s+=1
        if f < len(nums1):
            res.extend(nums1[f:])
        elif s < len(nums2):
            res.extend(nums2[s:])

        return res