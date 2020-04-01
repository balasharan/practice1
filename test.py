from git import Repo
import subprocess
# try:
#     repo_dir = 'practice1'
#     repo = Repo(repo_dir)
#     file_list = [
#         '/Users/isum/git/practise1/test',
#         #'/Users/isum/git/practice1/python_git.py'
#     ]
#     commit_message = 'Add simple regression analysis'
#     repo.index.add(file_list)
#     repo.index.commit(commit_message)
#     origin = repo.remote('origin')
#     origin.push()
# except git.GitCommandError as exception:
#     print(exception)
#     if exception.stdout:
#         print('!! stdout was:')
#         print(exception.stdout)
#     if exception.stderr:
#         print('!! stderr was:')
#         print(exception.stderr)


subprocess.check_output('git add .', shell=True)
subprocess.check_output('git commit -m "a commit"', shell=True)
