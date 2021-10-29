def func():
    num = 10
    print(f'在局部作用域中调用num局部变量：{num}')

func()
print(f'在全局作用域中调用num局部变量：{num}')