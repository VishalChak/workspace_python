
class Solution:
    def merge(self, arr, l , m , r ):
        n1  = m-l+1
        n2  = r-m
		
        L = [0] * n1
        R = [0] * n2
		
        for i in range(n1):
          L[i] = arr[l+i]
		
        for i in range(n2):
            R[i] = arr[m+i+1]
        
        i = 0
        j = 0
        k = l
		
        while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1
        
        while i < n1:
            arr[k] = L[i]
            i +=1
            k +=1
        
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            

    def merges(self, arr, l , r):
        # print(l , r)
        if l < r :
            m = (l+r)//2
            self.merges(arr, l, m )
            self.merges(arr, m+1, r )
            self.merge(arr, l , m , r)
            
        

    def mergeSort(self, arr):
        l = 0
        r = len(arr)-1
        # print(l ,r)
        self.merges(arr, l, r)
        return arr
        


if __name__ == "__main__":
    obj = Solution()
    arr=  [4,6,2,7,9,3,5,90,32]
    arr = obj.mergeSort(arr)
    print(arr)