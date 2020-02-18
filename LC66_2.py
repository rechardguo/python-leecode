from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       number=1
       for i in range(1,len(digits)+1):
           sum=digits[-i]+number
           digits[-i]=sum%10
           number=sum//10
           if number==0:
               return digits
       if number!=0:
           digits.insert(0,1)
       return digits

if __name__ == '__main__':
    print(Solution().plusOne([0]))
    print(1//10)

