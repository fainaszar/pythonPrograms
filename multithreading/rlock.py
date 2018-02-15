import threading

num = 0

print num
# lock = threading.Lock()

# lock.acquire()
# num+=1
# print num
# lock.acquire()
# num+=2
# print num
# lock.release()


lock = threading.RLock()

lock.acquire()
num += 3
print num
lock.acquire()
num += 4
print num
lock.release()
lock.release()
