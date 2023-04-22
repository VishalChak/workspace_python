# def sum(arr):


def sum_2(arr, target, i,j):
    temp_sum = arr[i] + arr[j]
    print(i, j , temp_sum)
    # if i>=j:
    #     return None
    if  (temp_sum == target ) or i+1 == j :
        return [arr[i] , arr[j]]
    elif temp_sum > target:
        j = j-1
        return sum_2(arr, target, i , j )
    else:
        i = i +1
        return sum_2(arr, target, i , j )


def sum_2_close(arr, target, i,j):
    temp_sum = arr[i] + arr[j]
    # print(i, j , temp_sum)
    # if i>=j:
    #     return None
    if  (temp_sum == target ) or (i+1) == j :
        return arr[i] , arr[j]
    elif temp_sum > target:
        j = j-1
        return sum_2_close(arr, target, i , j )
    else:
        i = i +1
        return sum_2_close(arr, target, i , j )

if __name__ == "__main__":
    arr = [1,3,1,-1,5,3,8,10,]
    arr.sort()
    print(arr)
    # print(sum_2(arr , 14, 0 , len(arr)-1 ))
    target = 15
    sum_3 = 0
    for k in range(len(arr)):
        a = arr[k]
        tar_2 = target - a
        res = sum_2_close(arr[:k] + arr[k+1:] , tar_2, 0 , len(arr)-2)
        print(tar_2, a , res)
        # if res == tar_2:
        #     print(target, "----")
        #     break
        # elif abs(target - res - a) < abs(target - sum_3):
        #     sum_3 = res + a

