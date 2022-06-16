# import os   # 功能系统交互
# import sys
# import hashlib
# import random
# import json
# import re  # 正则表达式
import logging
import os

mkdir_dir = os.path.dirname(__file__)
log_path = os.path.join(mkdir_dir, 'log')
username = 't1.log'
user_path = os.path.join(log_path, f'{username}')


#  日志的格式
logging.basicConfig(
    filename=user_path,  # 日志的存放位置
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
    # 定义日志格式
    datefmt='%y-%m-%d %X',
    # 输出日志的时间
    level=10
    # 报警级别
)

while True:
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    if username == 'user' and password == '123':
        logging.info(f'{username}用户登录成功')
        print(f'{username}用户登录成功')
        break;
    else:
        logging.error(f'{username}用户登录失败')
        print(f'{username}用户登录失败')
