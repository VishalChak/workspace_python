def n_que(que, l , n , cols ):
    if l == n:
        print("--------")
        for l in que:
            print(l)
    elif l ==0 :
        for i in range(n):
            que = [["." for x in range(n)] for y in range(n)]
            que[0][i] = "Q"
            # print(que, i)
            n_que(que, l+1, n, [i])
    else:
        for i in range(n):
            if i not in cols:
                if (i-1 >=0 and i+1 < n and que[l-1][i-1] !='Q' and que[l-1][i+1] !='Q' ) or (i-1 in range(n) and que[l-1][i-1] != 'Q') or (i+1 in range(n) and que[l-1][i+1] != 'Q') :
                    temp = que.copy()
                    temp[l][i] = 'Q'
                    temp_cols = cols.copy()
                    temp_cols.append(i)
                    n_que(temp, l+1, n , temp_cols)

        #     if que[l-1][i] != 'Q':
        #         if ( i-1 >=0 and i+1 < n and que[l-1][i-1] != 'Q' and que[l-1][i+1] != 'Q' ):
        #             temp = que.copy()
        #             temp[l][i] = 'Q'
        #             n_que(temp, l+1, n)
        #         elif ( i-1 < 0  and i+1 < n  and que[l-1][i+1] != 'Q' ):
        #             temp = que.copy()
        #             temp[l][i] = 'Q'
        #             n_que(temp, l+1, n)
        #         elif (i+1 >= n and i - 1 >= 0 and que[l-1][i-1] != 'Q'):
        #             temp = que.copy()
        #             temp[l][i] = 'Q'
        #             n_que(temp, l+1, n)

if __name__ == "__main__":
    n_que("", 0, 4, [])
    