password = input('请输入您的银行卡密码：')

if len(password) == 6 and password.isdigit():
    print('输入密码成功')
else:
    print('密码输入错误，请重新输入')
