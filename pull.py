try:
    git.Repo.clone_from(http://github.com/balasharan/practice1.git, /Users/Nisum/git/practice1/)
except git.GitCommandError as exception:
    print(exception)
    if exception.stdout:
        print('!! stdout was:')
        print(exception.stdout)
    if exception.stderr:
        print('!! stderr was:')
        print(exception.stderr)
