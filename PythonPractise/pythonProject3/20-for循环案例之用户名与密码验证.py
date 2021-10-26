# 第一种方法

# flag = 2
# while flag >= 0:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#
#     if username == 'admin' and password == 'admin888':
#         print("登陆成功")
#         break
#     else:
#         if flag == 0:
#             flag -= 1
#             continue
#         print(f'输入错误，还有{flag}次机会')
#     flag -= 1
# # 循环可以设置else，当循环条件不满足时执行else中的内容，并退出循环
# else:
#     print("输入错误，机会用完，登录失败")


# 第二种方法
#
# for flag in range(3):
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#
#     if username == 'admin' and password == 'admin888':
#         print("登陆成功")
#         break
#     else:
#         print(f'输入错误，还有{2-flag}次机会')
# # 循环可以设置else，当循环条件不满足时执行else中的内容，并退出循环
# else:
#     print("输入错误，机会用完，登录失败")


# 第三种方法
# 定义变量，用于记录登录次数
trycount = 0
# 循环3次，因为超过3次就会报错
for i in range(3):
    # 更新登录次数
    trycount += 1
    # 提示用户输入账号与密码
    username = input('请输入您的登录账号：')
    password = input('请输入您的登录密码：')

    # 判断用户名是否正确
    if username == 'admin':
        # 判断密码是否正确
        if password == 'admin888':
            print('恭喜你，登录成功')
            break
        else:
            print('密码错误')
            print(f'您还有{3 - trycount}次输入机会')
    else:
        print('用户名错误')
        print(f'您还有{3 - trycount}次输入机会')
