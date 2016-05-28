import time
t1 = time.time()
time.sleep(10)
t2 = time.time() - t1
print(time.ctime(t2))
print(time.strftime("%X", time.gmtime(t2)))