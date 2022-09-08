def wordSubsets( words1 , words2):
    res = []
    for i in range(len(words1)):
        flag = True
        for b in words2:
            a = words1[i]
            for ch in b:
                print(ch, a)
                if ch not in a:
                    flag = False
                    break
                else:
                    a = a.replace(ch, "", 1)
                print(a, flag, ch, "--")
            if not flag:
                break
        # print(flag)
        if flag:
            res.append(words1[i])
    return res
                    
if __name__ == "__main__":    
    print(wordSubsets(a,b))