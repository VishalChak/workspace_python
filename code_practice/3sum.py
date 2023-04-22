from itertools import combinations

def threesum(nums):
    str_len = "".join(str(val) for val in list(range(len(nums))))
    print(str_len) 
    a = combinations(str_len, 3)
    y = [''.join(i) for i in a]
    print(y)
    res = []
    for ind_set in y:
        if nums[int(ind_set[0])] + nums[int(ind_set[1])] + nums[int(ind_set[2])] == 0:
            a = [nums[int(ind_set[0])] , nums[int(ind_set[1])] , nums[int(ind_set[2])]]
            a.sort()
            if a not in res:
                res.append(a)
    # print(res)
if __name__ == "__main__":
    a = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    threesum(a)
