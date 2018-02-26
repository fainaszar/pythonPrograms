import os
import subprocess

currentDirectory = os.getcwd()

directoryContents = os.listdir(currentDirectory)

os.mkdir("Output") 

for content in directoryContents:
	if os.path.isdir(content):
		path = os.path.join(currentDirectory,content)
		files = os.listdir(path)
		for file in files:
			subprocess.Popen(["cp " + file , os.path.join(currentDirectory,"Output")],stdout=subprocess.PIPE)
			print "File {} copied".format(file)

