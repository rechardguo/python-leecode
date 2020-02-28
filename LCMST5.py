# coding=utf-8
# 有几个点：
# 1.range(x,y)  y 是不包括的
# 2.str="12"  str[1:3] 是为空的
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first)-len(second))>1:
            return False

        if len(first)==len(second):
            count=0
            for i in range(len(first)):
                if first[i:i+1]!=second[i:i+1]:
                    count+=1
                    if count==2:
                        return False
            return True
        else:
            p1=first if len(first)>len(second) else second
            p2=first if len(first)<len(second) else second
            for i in range(len(p1)):
                if p1[0:i]+p1[i+1:]==p2:
                    return True
            return False
if __name__ == '__main__':
    print(Solution().oneEditAway("ab","a"))