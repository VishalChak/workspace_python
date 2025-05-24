def find_pairs(arr, sum_):
    i = 0
    j = len(arr)-1
    arr.sort()
    res = []
    while (i <j):
        temp_sum = arr[i] + arr[j]
        print(arr[i], arr[j])
        if temp_sum == sum_:
            res.append([arr[i], arr[j]])
            i+=1
            j-=1
        elif temp_sum > sum_:
            j = j-1
        else:
            i = i+1
    return res
arr = [0, 2, 6, 3, 9, 11, 4.5, 4.5, 4.5, 4.5]
sum_ = 9
res = find_pairs(arr, sum_)
print(res)
    