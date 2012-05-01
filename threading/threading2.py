import threading
import time
class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        lock.acquire()
        for i in range(3):
            x=x+1
        time.sleep(2)
        print x
        lock.release()
    
    
if __name__=="__main__":
    lock=threading.RLock()
    x=0
    t1=[]
    for i in range(10):
        t=mythread(str(i))
        t1.append(t)
    for i in t1:
        i.start()
            