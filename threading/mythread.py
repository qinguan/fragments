import threading
import time 
class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        time.sleep(15)
        print self.getName()
def fun1():
    t1.start()
    print 'func1 done'
def fun2():
    time.sleep(2)
    t2.start()
    print 'func2 done'

if __name__=="__main__":
    t1=mythread('t1')
    t2=mythread('t2')
    t2.setDaemon(True)
    fun1()
    fun2()