import threading
import Queue
import time
import sys
import subprocess
import logging
from backports.shutil_get_terminal_size import get_terminal_size 

printq = Queue.Queue()
interrupt = False
lines = []


def main():

	ptt = threading.Thread(target=printer)
	ptt.daemon = True
	ptt.start()


	for i in xrange(1,50):
		printq.put(" ".join([str(x) for x in range(1,i) ]))
		
		time.sleep(.5)


def split_line(line,cols):

	if len(line) > cols:
		new_line = ''
		ww = line.split()
		i=0

		while len(new_line) <= (cols - len(ww[i]) -1):
			new_line += ww[i] + " "
			i += 1
			print len(new_line)

		if new_line == '':
			return(line,'')

		return(new_line,' '.join(ww[i:]))
	else:
		return(line,'')


def printer():

	while True:
		cols,rows = get_terminal_size()
		msg = "#"+"-"*(cols-2) + "#\n"
		try:
			new_line = str(printq.get_nowait())
			
			if new_line != '!@#EXIT#@!':
				lines.append(new_line)
				printq.task_done()
			else:
				printq.task_done()
				sys.exit()
		except Queue.Empty:
			pass



		for line in lines:
			res = line

			while len(res) !=0:
				toprint , res = split_line(res,cols)
				msg += '\n' + toprint



		subprocess.check_call('clear')
		sys.stdout.write(msg)
		sys.stdout.flush()
		time.sleep(0.5)

		


main()