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