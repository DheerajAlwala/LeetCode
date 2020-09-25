#1207. Unique Number of Occurrences
class Solution(object):
    def uniqueOccurrences(self, arr):
        d = dict()
        for c in arr:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        d1=dict()
        for v in d.values():
                if v not in d1:
                    d1[v]=1
                else:
                    d1[v]+=1
        if len(d)==len(d1):
            return True
        else:
            return False
            
        
        
        
