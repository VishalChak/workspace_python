def print_arr(arr):
    for i in range(len(arr)):
        for j in range (len(arr)):
            print(arr[i][j], end = " ")
        print()

def rotate(matrix):
    l = len(matrix)
    for x in range(0, l//2):
        
        for y in range(x, l-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][l-x-1]
            matrix[y][l-x-1] = matrix[l-x-1][l-y-1]
            matrix[l-x-1][l-y-1] = matrix[l-y-1][x]
            matrix[l-y-1][x] = temp
    
    print_arr(matrix)

if __name__ =="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    matrix = [[4,33,13,32,12,2],[24,1,7,33,27,29],[1,20,32,2,14,20],[6,28,32,27,25,26],[32,21,22,9,13,16],[34,7,26,14,21,28]]
    
    print_arr(matrix)
    print()
    rotate(matrix)