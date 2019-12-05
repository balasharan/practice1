#from git import Repo
import subprocess
a = 'qa'
text = 'qa12-012'
with open("test2", "a") as myfile:
    myfile.write(text)

if ( a == 'master' ):
    subprocess.check_output('git checkout master', shell=True)
    subprocess.check_output('git add .', shell=True)
    subprocess.check_output('git commit -m "1 commit"', shell=True)
    subprocess.check_output('git push origin master', shell=True)
else:
    subprocess.check_output('git checkout qa', shell=True)
    subprocess.check_output('git add .', shell=True)
    subprocess.check_output('git commit -m "2commit"', shell=True)
    subprocess.check_output('git push origin qa', shell=True)