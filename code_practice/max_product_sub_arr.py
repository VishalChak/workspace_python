def maxProduct(nums):
    ma = nums[0]
    mi = nums[0]
    ans = nums[0]
    for i in range(1 , len(nums)):
        val = nums[i]
        if val < 0:
            temp = ma
            ma = mi
            mi =temp

        ma = max(val , ma * val)
        mi = min(val , mi * val)
        if ans < ma:
            ans = ma
    return ans

if __name__ == "__main__":
    print(maxProduct([2,4,5,-2,4]))
