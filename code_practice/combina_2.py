def combinationSum2(candidates, target):
    res = []
    def dfs(cur , l, total ):
        if total== target:
            res.append(cur.copy())
            return
        if l >= len(candidates) and total > target:
            return
        
        for i in range(l,len(candidates)):
            cur.append(candidates[i])
            dfs(cur , i+1 , total+candidates[i])
            cur.pop()
    dfs([] , 0 , 0)
    res2 = []
    for i in range(len(res)):
        val = res[i]
        val.sort()
        if val not in res2:
            res2.append(val)
    print(res2)
        
if __name__ == "__main__":
    nums = [2,5,2,1,2]
    combinationSum2(nums, 5 )