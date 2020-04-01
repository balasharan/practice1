import subprocess
a = 'master'
text = 'qa1 \n'
with open("test", "a") as myfile:
    myfile.write(text)
try:
    if ( a == 'master' ):
        subprocess.check_output('git checkout -f master', shell=True)
        subprocess.check_output('git add .', shell=True)
        subprocess.check_output('git commit -m "111 commit"', shell=True)
        subprocess.check_output('git push origin master', shell=True)
    else:
        subprocess.check_output('git checkout qa', shell=True)
        subprocess.check_output('git add .', shell=True)
        subprocess.check_output('git commit -m "23132 th commit"', shell=True)
        subprocess.check_output('git push origin qa', shell=True)
except subprocess.CalledProcessError as error:
    print(error)
