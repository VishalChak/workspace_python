
def generate(s , op, clo, n , res):
    if op == n and clo == n:
        res.append(s)
    elif op < n and op == clo:
        generate(s+"(", op+1, clo, n, res)
    elif op < n and clo <op:
        generate(s+"(", op+1, clo, n, res)
        generate(s+")", op, clo+1, n, res)
    elif op==n and clo < n :
        generate(s+")", op, clo+1, n, res)
    return res


if __name__ == "__main__":
    res = generate('',0 ,0 , 3, [])
    print(res)