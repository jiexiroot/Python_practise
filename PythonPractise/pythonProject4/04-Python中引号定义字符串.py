name1 = '''I am Tome, Nice to meet you!'''
print(type(name1))
# 三引号支持换行
name2 = '''
    测试1
    I am Tom, Nice to meet you!
'''
name3 = """
    测试1
    I am Tom, Nice to meet you!
    I\'m tom, Nice to meet you!
"""

# 如果存在多个引号，建议① 单引号放在双引号中 ② 双引号放在单引号中。
print(name2)
print(name3)
