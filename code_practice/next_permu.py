def next_perm(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[i-1]:
            tempa = nums[:i]
            tempb = nums[i:]
            tempb.sort()
            temp = tempa[-1]
            tempa[-1] = tempb[0]
            tempb[0]=temp
            tempa.extend(tempb)
            nums = tempa
            return nums
    return nums



if __name__ == "__main__":
    print(next_perm([1,2,3]))