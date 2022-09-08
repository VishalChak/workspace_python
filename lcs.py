
def long_c_s(s,t):
    len_s = len(s)
    len_t = len(t)
    dp = [[0 for p in range(len_s+1)] for q in range(len_t+1)]
    dp_s = [["" for p in range(len_s+1)] for q in range(len_t+1)]
    
    mx = 0    
    res = ""
    for i in range(len_t+1):
        for j in range(len_s+1):
            if i==0 or j==0:
                pass
            elif s[j-1] == t[i-1]:
                dp[i][j] = dp[i-1][j-1] +1
                dp_s[i][j] = dp_s[i-1][j-1] + s[j-1]
            if dp[i][j] > mx:
                mx = dp[i][j]
                res = dp_s[i][j]
    return mx , res

if __name__ == "__main__":
    s = "ac"
    t = "ca"
    print(long_c_s(s, t))
