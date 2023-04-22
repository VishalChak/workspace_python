def countSay(n, res):
    if n ==1:
        res = "1"
    else:
        x = countSay(n-1, res)
        f_count = 0
        for i in range(len(x)):
            if i ==0:
                f_count =1
            elif x[i] == x[i-1]:
                f_count += 1
            else:
                res = res+ str(f_count) +x[i-1]
                f_count =1
        if f_count >0:
            res = res + str(f_count) +x[-1]
    return res

if __name__ == "__main__":
    print(countSay(10 , ""))

            