import threading
import time
class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
##        time.sleep(5)
##        print self.num
        print self.getName()
        
def func():
    t.start()
    print t.isAlive()
##    t.join()
##    for i in range(5):
##        print i
    
if __name__=="__main__":
    t=mythread("t1")
    t.start()
    t.setName('T')
    print t.getName()
    t2=mythread('t2')
    t2.start()
    
##    print t.getName()
##    func()