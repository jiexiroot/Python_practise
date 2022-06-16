# 弹窗恶搞
import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('2022新年快乐')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='2021新年快乐！',  # 标签的文字
             bg='Red',  # 背景颜色
             font=('楷体', 17),  # 字体和字体大小
             width=15, height=2  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()


k = 0
threads = []
while True:  # 需要的弹框数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[k].start()
    k += 1
    if k == 150: break
