class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:

        if len(s1)!=len(s2): return False
        tmp={}
        for s in s1:
            if tmp[s]==None:
                tmp[s]=1
            else:
                tmp[s]+=1

        for s in s2:
            if tmp[s]==None or tmp[s]==0:
                return False
            else:
                tmp[s]-=1

        return True