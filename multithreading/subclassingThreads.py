import logging
import threading

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s'
					)

class MyThread(threading.Thread):

	def run(self):
		logging.debug('Running')
		return

class MyThreadWithArgs(threading.Thread):

	def __init__(self,group=None,target=None,name=None,
				 args=(),kwargs=None,verbose=None):

		threading.Thread.__init__(self,group=group,target=target,name=name,
									verbose=verbose)

		self.args = args
		self.kwargs = kwargs
		return


	def run(self):
		logging.debug('running with %s and %s',self.args,self.kwargs)
		return




for i in range(5):
	t = MyThread()
	t2 = MyThreadWithArgs(args=(i,),kwargs={'a':'A','b':'B'})
	t.start()
	t2.start()