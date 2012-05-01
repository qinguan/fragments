import pickle
import string

fp=open(r'C:\Users\qinguan\Desktop\banner.p','rb')
data=pickle.load(fp)
#result=""
#for i in data:
    #for j in i:
        #result+=j[0]*j[1]
    #print result+'\n'
    #result=""
buf = ''
for line in data:
    for char in line:
        buf += char[0]*char[1]
    print buf + '\n'
    buf = ''

