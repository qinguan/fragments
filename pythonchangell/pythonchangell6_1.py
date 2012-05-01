import zipfile

f=zipfile.ZipFile(r"C:\Users\qinguan\Desktop\channel.zip","r")
num="90052"
file=num+'.txt'
comment=""
for i in range(100000):
    comment+=f.getinfo(file).comment
    num=f.read(file).split()[-1]
    file=num+'.txt'
    if file =='46145.txt':
        break
file_out=open(r"C:\Users\qinguan\Desktop\2.txt","w")
file_out.write("  ".join(comment))


    