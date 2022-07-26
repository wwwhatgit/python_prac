import os
os.getcwd()
os.chdir('c:\\Users\\wwwha\\Python')
import git
git.Repo.clone_from('https://github.com/wwwhatgit/python_prac.git', 'python_prac')
my_repo = git.Repo('python_prac')



my_repo.git.add('--all')
my_repo.git.commit('-m', 'add file for git command', author='Karl')
origin = my_repo.remote(name='origin')
origin.push()