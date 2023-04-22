def romanToInt(s):
    roman_dict = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
    # print(len(s))
    s_len = len(s)
    # max_ch = ""
    sum_ro = 0
    for i in range(len(s)):
        ch = s[s_len-i-1]
        # print(ch)
        if i ==0:
            print(ch, i, "+")
            sum_ro += roman_dict[ch]
            
        else:
            if roman_dict[ch] >= roman_dict[s[s_len-i]]:
                print(ch, i, "+", roman_dict[ch], roman_dict[s[s_len-i-2]])
                sum_ro += roman_dict[ch]
            else:
                print(ch, i, "-", roman_dict[ch], roman_dict[s[s_len-i-2]])
                sum_ro -= roman_dict[ch]
        print("-----------")
    print(sum_ro)

    

if __name__ == "__main__":
    romanToInt("MMMCMXCIX")