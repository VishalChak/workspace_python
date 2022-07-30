def closest_num(arr):
    clo = None
    for i in range(1, len(arr)):
        if arr[i] > arr[0] and clo == None:
            clo = i
        elif arr[i] > arr[0]:
            if arr[i] - arr[0] < arr[clo] - arr[0]:
                clo = i
    temp = arr[0]
    arr[0] = arr[clo]
    arr[clo] = temp
    temp = arr[:1]
    temp_1 = arr[1:]
    temp_1.sort()
    temp.extend(temp_1)
    # print(temp_1)
    return temp


def nextGreaterPermutation(arr):
    # print(arr)
    for i in range(len(arr)):
        if arr[-1-i] < max(arr[-1-i:]):
            temp = arr[:-1-i]
            temp.extend(closest_num(arr[-1-i:]))
            return temp
    return arr


if __name__ == "__main__":
    arr = [3,1,5,4,3,2,1]
    print(arr)
    print(nextGreaterPermutation(arr))