


if __name__ == "__main__":
    x = 4
    
    k = 0 
    m = x
   
    l = 0
    n = x
    print("vishal")


    while (k < m and l < n):
        
        for i in range(l, n):
            print(k, i)
        k +=1 
        
        print()
        
        for i in range( k, m):
            print(i , n-1)
        n -=1
        
        print()

        if ( k < m ):
            for i in range(n-1, l-1, -1):
                print(m-1, i)
            m -=1
        print()
        if ( l< n ):
            for i in range(m-1 , k-1, -1):
                print(i, k-1)
        print()
        # break
    