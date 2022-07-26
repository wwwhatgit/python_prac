# Valid Anagram leet code 242
from re import S


class Solution:
    def __init__(self, s1, t1):
       self.str = s1
       self.tr = t1
    def isAnagram(self):
        s = self.str
        t = self.tr
        if len(s) != len(t):
            return False

        countStr={}
        for i in range(len(s)):
            countStr[s[i]] = 1+countStr.get(s[i],0)   
        for i in range(len(t)):
            countStr[t[i]] = countStr.get(t[i],0)-1

        for key,value in countStr.items():
            if value!=0:
                return False
        return True
    

        

sr = 'anagram'
tr = 'nagaram'

sol = Solution(sr,tr)
sol.isAnagram()
