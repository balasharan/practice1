#from git import Repo
import subprocess
a = 'qa'
if ( a == 'master' ):
    subprocess.check_output('git checkout master', shell=True)
    subprocess.check_output('git add .', shell=True)
    subprocess.check_output('git commit -m "1 commit"', shell=True)
    subprocess.check_output('git push origin master', shell=True)
else:
    subprocess.check_output('git checkout qa', shell=True)
    subprocess.check_output('git add .', shell=True)
    subprocess.check_output('git commit -m "1 commit"', shell=True)
    subprocess.check_output('git push origin qa', shell=True)