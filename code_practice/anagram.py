class Solution:
    def check_ana(self, str1, str2):
        sd = {}
        for ch in str1:
            if ch in sd:
                sd[ch] = sd[ch] +1
            else:
                sd[ch] = 1
        
        for ch in str2:
            if ch in sd:
                sd[ch]= sd[ch] - 1
            else:
                return False
        
        for key in sd:
            if sd[key] != 0:
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indx = [False] * len(strs)
        val_dict = {}
        for i in range(len(strs)):
            val_dict[i] = []
            
        for i in range(len(strs)):
            for j in range(len(strs)):
                if not indx[j] :
                    if i == j:
                        indx[i] = True
                        val_dict[i].append(strs[j])
                    elif self.check_ana(strs[i], strs[j]):
                        indx[j] = True
                        val_dict[i].append(strs[j])
            # print(indx)
        res = []
        
        # print(len(val_dict))
        for key in val_dict:
            if len(val_dict[key])> 0:
                res.append(val_dict[key])
        return res