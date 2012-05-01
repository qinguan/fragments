import os 
import Image
from cStringIO import StringIO

os.chdir(r"C:\Users\qinguan\Desktop")
s = open("evil2.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]  # every fifth byte, starting at i
    im = Image.open(StringIO(piece))
    f = open("%d.%s" % (i, im.format.lower()), "wb")
    f.write(piece)
    f.close()
