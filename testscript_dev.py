import subprocess
def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)

branch_name = 'dev'
version_text = 'working code - eway \n'

if ( branch_name == 'master' ):
    with open("version_file", "w") as myfile:
        myfile.write(version_text)
    subprocess_cmd('git checkout -f master')
   
elif (branch_name == 'dev'):
    with open("version_file", "w") as myfile:
        myfile.write(version_text)
    subprocess_cmd('git checkout -f dev')
else:
    with open("version_file", "w") as myfile:
        myfile.write(version_text)
    subprocess_cmd('git checkout -f qa')


if ( branch_name == 'master' ):
    subprocess_cmd('git checkout -f master; git add version_file; git commit -m "111 commit";git push origin master')
elif (branch_name == 'dev'):
    subprocess_cmd('git checkout -f dev; git add version_file; git commit -m "1101 commit";git push origin dev')
else:
    subprocess_cmd('git checkout -f qa; git add version_file; git commit -m "111133 commit";git push origin qa')

