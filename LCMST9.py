# coding=utf-8
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False

        index=0
        for s in s1:
            if s==s2[0:1]:
                break
            index+=1

        rs=s1[index:]+s1[0:index]
        return rs==s2

if __name__ == '__main__':
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(Solution().isFlipedString(s1,s2))
