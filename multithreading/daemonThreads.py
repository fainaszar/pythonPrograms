import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s')


def daemon():
	logging.debug('Starting')
	time.sleep(2)
	logging.debug('Exiting')

d= threading.Thread(name='Daemon',target=daemon)
d.setDaemon(True)



def non_daemon():
	logging.debug('Starting')
	logging.debug('Exiting')



t = threading.Thread(name='Non_Daemon',target=non_daemon)

d.start()
t.start()


#Wait for daemon thread to exit

d.join(3)
#t.join()

print 'Is d Alive: ' , d.isAlive()
t.join()


