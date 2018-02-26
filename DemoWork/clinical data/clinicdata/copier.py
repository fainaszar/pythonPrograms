import os
import subprocess
import time
start = time.time()
currentDirectory = os.getcwd()

directoryContents = os.listdir(currentDirectory)
outpath = os.path.join(currentDirectory,"Output")
os.mkdir("Output") 

count = 0
for content in directoryContents:
	if os.path.isdir(content):
		path = os.path.join(currentDirectory,content)
		files = os.listdir(path)
		for file in files:
			filepath = os.path.join(path,file)
			
			subprocess.Popen(["cp",filepath,outpath],stdout=subprocess.PIPE)
			count+=1

print "Completed copying {} files in {} seconds".format(count,time.time()-start)