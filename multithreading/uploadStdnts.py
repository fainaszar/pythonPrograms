import subprocess
import math

from multiprocessing import Pool
from datetime import datetime
from upload import schools

start = datetime.now()

print start.time() , "STARTED PROCESSING".center(80,"-")

no_schools = len(schools)
print(no_schools)


def runProcess(school_number):
	subprocess.call(['python','uploadStd.py',str(school_number)])



if __name__ == '__main__':
	p = Pool()
	for school_number in xrange(1,no_schools+1):
		p.apply_async(runProcess,args=(school_number,))

	p.close()
	p.join()

end = datetime.now()
print end.time() , "ENDING PROCESS".center(80,"-")
print "Completed in {} seconds".format((end-start).total_seconds())