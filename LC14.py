from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        s1=min(strs)
        s2=max(strs)
        for k,v in enumerate(s1):
            if v!=s2[k]:
                return s1[:k]
        return s1
