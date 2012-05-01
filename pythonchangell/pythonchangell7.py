import Image
print Image.open(r"C:\Users\qinguan\Desktop\oxygen.png").tostring()[108188:110620:28]
#im=Image.open(r"C:\Users\qinguan\Desktop\oxygen.png")
#result=[] 
#y_begin = 0
#while True:
    #p = im.getpixel((0, y_begin))
    #if p[0] == p[1] == p[2]:
        #break
    #y_begin += 1
#x_end = 0
#while True:
    #p = im.getpixel((x_end, y_begin))
    #if not p[0] == p[1] == p[2]:
        #break    
    #x_end += 1
#for i in range(0,x_end,7):
    #p = im.getpixel((i, y_begin))
    #result.append(chr(p[0]))
#print "".join(result)
#hint=[105, 110, 116, 101, 103, 114, 105, 116, 121]
#print "".join([chr(c) for c in hint])