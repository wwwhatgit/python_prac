import os
os.getcwd()
os.chdir('c:\\Users\\wwwha\\Python')
import git
git.Repo.clone_from('https://github.com/wwwhatgit/python_prac.git', 'python_prac')
my_repo = git.Repo('python_prac')

with my_repo.config_writer() as git_config:
    git_config.set_value('user', 'email', 'wwwhat1101@gmail.com')
    git_config.set_value('user', 'name', 'Karl Ma')
with my_repo.config_reader() as git_config:
    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))

my_repo.git.add('--all')
my_repo.git.commit('-m', 'init change ', author='Karl')
origin = my_repo.remote(name='origin')
origin.push()

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
