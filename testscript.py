import subprocess
def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)

branch_name = 'dev'
text = 'qa12-24445wertyuytrjhgf1234567890-de \n'
with open("test_1", "w") as myfile:
    myfile.write(text)

branch_name = 'dev'
subprocess_cmd('git checkout -b "$branch_name"; git add .; git commit -m "111 commit";git push origin $branch_name')