import time

s_size = 0
d_size = 1025444

while s_size < d_size:
    # 每次下载1024个字节
    # 实心的是 9632 空心的是 9633
    s_size += 1024
    time.sleep(0.01)
    x = s_size / d_size
    if x > 1:
        x = 1
    y = int(x * 50) * chr(9632)
    z = int(50 - x * 50) * chr(9633)
    print('\r[%-50s]%d%%' % (y + z, x * 100), end='')
