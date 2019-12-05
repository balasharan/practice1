from git import Repo

repo_dir = 'practice1'
repo = Repo(repo_dir)
file_list = [
    '/Users/Nisum/git/practise1/test',
     #'/Users/Nisum/git/practice1/python_git.py'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
