

def intToRoman(num):
    int_dict = {1:"I", 4:"IV",5:"V", 9:"IX",10:"X", 40:"XL",50:"L", 90:"XC",100:"C" , 400:"CD", 500: "D", 900:"CM", 1000:"M"}   
    arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman = ""
    for i in range(len(arr)):
        inx = num//arr[i]
        num = num - arr[i] * inx
        if inx > 0 :
            roman += "".join([int_dict[arr[i]]] * inx)
    print(roman)



if __name__ == "__main__":
    intToRoman(3999)
    # arr = ["#"] * 5
    # print(arr)