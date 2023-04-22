
def permutation(l , r, nums, res):
    if l == r:
        x = ','.join([str(i) for i in nums])
        if x not in res:
            res.append(x)
    else:
        for i in range(l, r):
            nums[i], nums[l]= nums[l], nums[i]
            permutation(l+1, r, nums, res)
            nums[i], nums[l]= nums[l], nums[i]

if __name__ == "__main__":
    res = []
    nums = [1,2,3]
    permutation(0, len(nums), nums, res)
    print(res)