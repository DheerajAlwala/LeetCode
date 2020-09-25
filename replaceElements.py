#1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr):
        ls=[]
        for i in range(len(arr)-1):
            ls.append(max(arr[i+1:]))
        ls.append(-1)
        return ls
