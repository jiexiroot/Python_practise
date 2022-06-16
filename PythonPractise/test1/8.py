import hashlib


# 密码加盐 afbee3d88db54c0f08c18f78799492c0  d85f4415535503a37e4375c45c79726a


def hash(x, y):
    password = hashlib.md5()
    password.update(x.encode('utf-8'))
    password.update(y.encode('utf-8'))
    return password.hexdigest()


s = hash('xm19891009', '宝塔镇河妖')
print(hash('xm19891009', '宝塔镇河妖'))
#
# list1 = ['123123', '413123', 'xh123123', '345612', 'desadsdas', 'dsadasdasd', 'dsadasfg', 'xm19891009']
#
# dict = {}
# for i in list1:
#     dict[i] = hash(i)
#
# print(dict)
#
#
# for k, v in dict.items():
#     if dict[k] == y:
#         print('撞库成功，密码为%s', k)
#     else:
#         print('撞库失败')
