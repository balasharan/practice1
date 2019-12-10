import subprocess
def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)

a = 'master'
text = 'qa12-22 \n'
with open("test", "a") as myfile:
    myfile.write(text)

subprocess_cmd('git checkout -f master; git add .; git commit -m "111 commit";git push origin master')