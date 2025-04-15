class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(arr, res, i):
            if arr == []:
                # print("if", res)
                return res.append([i])
            else:
                dfs(arr[0:-1], res, arr[-1])
                # print(arr, res, i)
                # print("else",res)
                for k in range(len(res)):
                    q = res.pop(0)
                    l = q[:]
                    # print("k",k,"r", res)
                    for j in range(len(q)+1):
                        l.insert(j, i)
                        # print("ch_l",l, "q", q)
                        res.append(l)
                        # print("j",j,"r",res)
                        l = q[:]
                        # print("q", q, "l", l)

                return res

        res = []

        dfs(nums[0:-1],res, nums[-1])

        return res