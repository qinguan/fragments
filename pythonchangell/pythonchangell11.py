import ImageEnhance
import Image
im=Image.open(r"C:\Users\qinguan\Desktop\cave.jpg")
enhancer = ImageEnhance.Brightness(im)
factor = 8
enhancer.enhance(factor).show()
