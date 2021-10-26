username = input('请输入您的用户名（只能为密码+数字形式）：')

if username.isalnum():
    print('合理的用户名，正在录入系统...')
else:
    print('输入的用户名有误，请重新输入...')
