def getInversionCount(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                print(array[i], array[j])


if __name__ == "__main__":
    arr = [8,4,]
    getInversionCount(arr)