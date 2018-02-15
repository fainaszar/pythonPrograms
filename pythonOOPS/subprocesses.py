from subprocess import Popen,PIPE

process = Popen(['cat','basic.py'],stdout=PIPE,stderr=PIPE)
stdout,stderr = process.communicate()


import subprocess
#subprocess.call(["ls","-l"])

output = subprocess.check_output(["ls","-l"])
print output.replace(".py",".cpp").replace("1","2").replace("faizan","Admin")