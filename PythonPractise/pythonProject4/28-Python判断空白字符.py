str1 = ' '  # 最少要包含一个空白字符
print(str1.isspace())

username = input('请输入的您的用户名：')
if len(username) == 0 or username.isspace():
    print('您没有输入任何字符...')
else:
    print(f'您的输入的字符：{username}')

if not username.isspace():
    print(f'您的输入的字符：{username}')
else:
    print('您没有输入任何字符...')
