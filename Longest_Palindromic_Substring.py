def longest_coman_substring(s):
    lens = len(s)
    dp = [[0 for i in range(lens)] for j in range(lens) ]
    
    for i in range(lens):
        dp[i][i] = 1
        if i+1 < lens and s[i] == s[i+1]:
            dp[i][i+1] = 1
    
    for i in range(2 , lens):
        for j in range(0, lens):
            if i+j >= lens:
                break
            elif s[j] == s[i+j] and dp[j+1][i+j-1] ==1:
                dp[j][i+j] = 1
    # for ll in dp:
    #     print(ll)
    max_len = 0
    res = ""
    for i in range(lens):
        for j in range(lens):
            if dp[i][lens-j-1] == 1 and max_len < lens-j-i:
                max_len = lens-j-i
                # print(max_len, i,lens-j,  s[i:lens-j])
                res = s[i:lens-j]
    return res


if __name__ == "__main__":
    s = "ibawpzhrunsgfobmenlqlxnprtgijgbeicsuoihnmcekzmvtffmlpzuwlimuuzjhkzppmpqqrfwyrjrsltkypjpcjffpvhtdiwjdonutobpecsiqubiusvwsyhrddqjeqqpgofifmwvmcdjixjvjxrvyabqaqumfqiiqxizmhzevhxutsbgzcfggyyvolwaxfcpjhfpksxvgyxhddcssnxhygzvmyxrxqizzhpluxkautjmieximoskcffimctsfzgmihtoxkltopwobtfjvjymtuknxmsgevkeklprcaudidywwkfuhtatpeeiewczpwiegmpjquayfleczrvzekikbaeocpcurtxhcsysbbsyschxtrucpcoeabkikezvrzcelfyauqjpmgeiwpzcweieeptathufkwwydiduacrplkekvegsmxnkutmyjvjftbowpotlkxothimgzfstcmiffcksomixeimjtuakxulphzziqxrxymvzgyhxnsscddhxygvxskpfhjpcfxawlovyyggfczgbstuxhvezhmzixqiiqfmuqaqbayvrxjvjxijdcmvwmfifogpqqejqddrhyswvsuibuqiscepbotunodjwidthvpffjcpjpyktlsrjrywfrqqpmppzkhjzuumilwuzplmfftvmzkecmnhiousciebgjigtrpnxlqlnembofgsnurhzpwabi"
    # print(s[1:3])
    print(longest_coman_substring(s))

