
from re import A


def spiralOrder(arr):
    k = 0
    m = len(arr)
    l = 0
    n = len(arr[0])

    while(k < m and l < n):
        for i in range(l, n):
            print(arr[k][i])
        k +=1

        for i in range(k , m):
            print(arr[i][n-1])
        
        n -=1

        if (k<m):
            for i in range(n-1, l-1, -1):
                print(arr[m-1][i])

            m -=1
        if (l < n):
            for i in range(m-1 , k-1, -1):
                print(arr[i][l])
            l +=1




if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    spiralOrder(arr)