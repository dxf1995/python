from PIL import Image, ImageTk
import time
import random
import math
import tkinter

root = tkinter.Tk()
# 绘制一个画布
cv = tkinter.Canvas(root, heigh=457, width=690)

# 背景图
image = Image.open("20210125005206.png")
photo = ImageTk.PhotoImage(image)

# 在画板上绘制一张图片

cv.create_image(0, 0, image=photo, anchor='nw')
cv.pack()
