import itertools


def getPare(n):
    i = 0
    x = ""
    while i <n:
        x = x +"("
        i +=1
    while (i > 0):
        x = x+ ")"
        i -=1
    y = ""
    # if n > 2:
    #      y = "("
    #      y = "(" + "".join(["()" for i in range(n-1)]) +")"
    # print(y)
    return x
    


def generator(input, res):
    permu = list(set(itertools.permutations(input)))
    res.extend(permu)
    for i in range(len(input)):
        if input[i] > 1 :
            input[i] = input[i] -1
            input.append(1)
            generator(input, res)
            break
    return res
    
def generateParenthesis(n):
    res = generator([n], [])
    res2  = []
    for arr in res:
        temp = ""
        for val in arr:
            temp = temp + getPare(val)
        res2.append(temp)
    return res2

if __name__ == "__main__":
    print(generateParenthesis(4))