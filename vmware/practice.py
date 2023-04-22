
def reverse_str_arr(arr):
    print(arr[::-1])


def armstrong(x):
    y = 0
    for val in str(x):
        y = y + (int(val) ) ** len(str(x))
    if y == x:
        print('Yes')
    else:
        print('No') 

## Sieve of Eratosthenes
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            print(p)


def lcs_len(a,b, i,j):
    if i ==0 or  j == 0 :
        return 0
    elif a[i-1]  == b[j-1 ]:
        return 1 + lcs_len(a, b , i-1, j-1)
    else:
        return max( lcs_len(a,b, i-1, j) , lcs_len(a,b,i, j-1))
    
def max_len(a , b):
    if len(a)> len(b):
        return a
    else:
        return b
    
    
def print_lcs(a,b, i,j):
    if i ==0 or  j == 0 :
        return ''
    elif a[i-1]  == b[j-1 ]:
        return print_lcs(a, b , i-1, j-1 ) + a[i-1]
    else:
        return max_len( print_lcs(a,b, i-1, j) , print_lcs(a,b,i, j-1))
    


def lcs_dp(a,b):
    dp = [[0] *  ( len(a) +1 ) ] * (len(b) +1 )
    print(dp)
    
    for i in range(1, len(a)+1):
        for j in range(1 , len(b)+1):
            if a[i-1] == b[j-1]:
                dp[j][i] = 1 + dp[j-1][i-1]
            else:
                dp[j][i] = max( dp[j][i-1] , dp[j-1][i])
    
    for i in range(1, len(a)+1):
        for j in range(1 , len(b)+1):
            print(dp[j][i] , end=" ")
        print()

from sys import maxsize
def max_sub_array(arr):
    max_so_far = -maxsize -1
    max_ending_here = 0 

    for val in arr:
        max_ending_here = max_ending_here + val

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0 :
            max_ending_here = 0

    return max_so_far






if __name__ == "__main__":
    # SieveOfEratosthenes(50)
    # reverse_str_arr(arr)
    # armstrong(154)

    a = '12341'
    b = '341'
    # print(lcs_len(a,b, len(a) , len(b) ))
    # print(print_lcs(a,b, len(a) , len(b) ))
    # lcs_dp(a,b)
    
    
    arr = [2,3,-1, 1,]
    print(max_sub_array(arr))    