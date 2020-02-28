# coding=utf-8
class Solution(object):
    def replaceSpaces(self, S, length):
       '''
       :param S:
       :param length:
       :return:
       '''
       return "%20".join(S[:length].split(" "))
