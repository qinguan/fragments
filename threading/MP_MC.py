import threading
import time
import Queue
class Produce(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global queue
        queue.put(self.getName())
        print self.getName(),'put',self.getName(),'to queue'

class Consumer(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global queue
        print self.getName(),'get',queue.get(),'from queue'

if __name__=="__main__":
    queue=Queue.Queue()
    plist=[]
    clist=[]
    for i in range(10):
        p=Produce('Produce'+str(i))
        plist.append(p)
    for i in range(10):
        c=Consumer('Consumer'+str(i))
        clist.append(c)
    for i in plist:
        i.start()
        i.join()
    for i in clist:
        i.start()
        i.join()
