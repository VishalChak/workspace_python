def largestContiguousSum( arr):
    conti_sum = []
    for i in range(1, len(arr)):
        j = 0 
        
        while (j +i <= len(arr)):
            print(arr[j : j+i])

            conti_sum.append(sum(arr[j : j+i]))
            print(conti_sum)
            j +=1
    conti_sum.append(sum(arr))
    print(conti_sum)
    
    return max(conti_sum)
if __name__ == "__main__":
    arr =  [1, -2, 3, 4, -5]
    # arr = [1,2,3,4,5]
    print(largestContiguousSum(arr))