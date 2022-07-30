def test(x):
    x = str(x)
    rev = ""
    mux = ""
    for i in range(len(x)-1, 0):
        if x[i] in ["-", "+"]:
            mux = mux + x[i]
        print(x[i])
if __name__ == "__main__":
    print(-2**31)