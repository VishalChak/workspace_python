def next_big(y, a):
    y.sort()
    for i in range(len(y)):
        val = y[i]
        if val> a:
            y[i] = a
            a = val
            return y, a 

def print_permu (arr, n):
    for i in range(n, 1 , -1):
        if arr[i-1] > arr[i-2]:
            x = arr[:i-1]
            y = arr[i-1:]
            y , x[-1] = next_big(y, x[-1])
            x.extend(y)
            return x


if __name__ == "__main__":
    n = 3
    k = 210
    # arr = [1,2,3] 
    arr = [i for i in range(1, n+1)]
    for i in range(k-1):
        arr = print_permu(arr, n)
    print(arr)

