str1 = 'hello'


def func():
    print(f'在局部作用域中调用str1变量：{str1}')


print(f'在全局作用域中调用str1变量：{str1}')
func()
