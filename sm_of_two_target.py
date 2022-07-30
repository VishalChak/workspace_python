from msilib.schema import tables


def twoSum(A, target):
    val_map = {}
    for i in range(0, len(A)):
        if A[i] not in val_map:
            val_map[A[i]] = [i]
        else:
            temp = val_map[A[i]]
            temp.append(i)
            val_map[A[i]] = temp
    # print(val_map)
    
    for i in range(0, len(A)):
        val = target - A[i]
        
        if (val in val_map)  and A[i] != val:
            return [i, val_map[val][0]]
        elif (val in val_map)  and A[i] == val:
            if len(val_map[val]) > 1:
                return [i, val_map[val][1]]


if __name__ == "__main__":
    A = [1, 3, 3, 4]
    target = 6
    print(twoSum(A, target))    

    
     