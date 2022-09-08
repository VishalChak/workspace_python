# def combination(combi ,l, nums, x, res):
#     if len(combi)==x:
#         res.append([int(ch) for ch in combi])
#     else:
#         for i in range(l , len(nums)):
#             combination(combi+str(nums[i]) , i+1, nums, x , res)


# if __name__ == "__main__":
#     nums = [1,2,3,4,5]
#     res = []
#     combination("", 0, nums, 2, res)
#     print(res)

def combination(combi ,l, nums, x, res):
    if sum([int(ch) for ch in combi]) == x:
        res.append([int(ch) for ch in combi])
    else:
        for i in range(l , len(nums)):
            combination(combi+str(nums[i]) , i+1, nums, x , res)


if __name__ == "__main__":
    nums = [10,1,2,7,6,1,5]
    res = []
    combination("", 0, nums, 8, res)
    print(res)
    # print(sum(nums))