str1 = 'hello world and hello python and hello linux'
# 不限定字符串长度
ands1 = str1.count('and')
# count("字符串", 出现的上标, 出现的下标)
ands2 = str1.count('and', 10, 30)
print(f'and字符出现的次数为{ands2}')
