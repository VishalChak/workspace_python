def longestCommonPrefix(strs):
    lo_pre = ""
    min_len  = min([len(val) for val in strs])
    
    for i in range(min_len):
        ch = ""
        if i <= len(strs)+1:
            ch = strs[0][i]
        for j in range(len(strs)):
            print(strs[j][i], ch)
            if strs[j][i] != ch:
                return lo_pre
        lo_pre = lo_pre + ch
    print(lo_pre)
    return lo_pre

if __name__ =="__main__":
    arr = ["flower","flower","flower","flower"]
    res = longestCommonPrefix(arr)
    print(res)
