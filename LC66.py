from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1,len(digits)+1):
            if digits[-i] !=9:
                digits[-i]=digits[-i]+1
                return digits
            digits[i]=0
        digits=[1]+digits
        return digits

if __name__ == '__main__':
    print(Solution().plusOne([0]))

