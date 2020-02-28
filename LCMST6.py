# coding=utf-8
class Solution:
    def compressString(self, S: str) -> str:
        # if S==None:
        #     return None
        # if not S:
        #     return ""
        if not S: return S
        count=1
        tmp=None
        st=""
        for c in S:
            if tmp!=c:
                if tmp==None: # 第一次遇到
                    tmp=c
                else:
                    st+=tmp+str(count)
                    tmp=c
                    count=1
            else:
                count+=1
        st+=tmp+str(count)  # 处理结尾
        return S if len(st)>=len(S) else st