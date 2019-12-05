#from git import Repo
import subprocess
subprocess.check_output('git add .', shell=True)
subprocess.check_output('git commit -m "a commit"', shell=True)
subprocess.check_output('git push origin master', shell=True)