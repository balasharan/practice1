#from git import Repo
import subprocess
a = 'qa'
text = 'qa12-16 \n'
# with open("test2", "a") as myfile:
#     myfile.write(text)

if ( a == 'master' ):
    with open("test", "a") as myfile:
        myfile.write(text)
    subprocess.check_output('git checkout master', shell=True)
    subprocess.check_output('git add .', shell=True)
    subprocess.check_output('git commit -m "2 commit"', shell=True)
    subprocess.check_output('git push origin master', shell=True)
else:
    with open("test2", "a") as myfile:
        myfile.write(text)
    subprocess.check_output('git checkout qa', shell=True)
    subprocess.check_output('git add .', shell=True)
    subprocess.check_output('git commit -m "7 th commit"', shell=True)
    subprocess.check_output('git push origin qa', shell=True)