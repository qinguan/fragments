import os
import string

dir=r"C:\Users\qinguan\Desktop\channel"
os.chdir(dir)
files=os.listdir(dir)
num="94191"
file=num+".txt"

while 1:
    try:
        content=open(file).readline().split()[-1]
        print content
        if content.isdigit():
            num=content
            file=num+".txt"
        else:
            break
    except:
        print 'wrong'
        break