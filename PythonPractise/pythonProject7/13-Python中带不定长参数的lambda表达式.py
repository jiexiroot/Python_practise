fn = lambda *args: args[1]
print(fn(10, 20, 30))


fn1 = lambda **kwargs: kwargs
fn2 = lambda **kwargs: kwargs['name']

print(fn1(name='杰希', age=18, address='四川省成都市'))
print(fn2(name='杰希', age=18, address='四川省成都市'))
