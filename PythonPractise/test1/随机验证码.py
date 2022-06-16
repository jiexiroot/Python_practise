import random

# for i in range(3):
#     x = str(random.randint(0, 9))
#     y = chr(random.randint(65, 98))
#     z = x + y
#     print(z, end='')

# randomint = random.randint(100000, 999999)
# print('\n', randomint)

# 模拟下载以及打印进度条

from time import sleep
from tqdm import tqdm

# # 这里同样的，tqdm就是这个进度条最常用的一个方法
# # 里面存一个可迭代对象
# for i in tqdm(range(1, 500)):
#     # 模拟你的任务
#     sleep(0.01)
# sleep(0.5)

import sys
import time


def progress_bar():
    for i in range(1, 101):
        print("\r下载: {}%: ".format(i), "▋" * (i // 2), end="")
        # sys.stdout.flush()
        time.sleep(0.05)


def test1():
    for i in range(5):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(1)


if __name__ == '__main__':
    # progress_bar()
    test1()
