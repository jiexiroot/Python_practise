# def func(name):
#     print(name)
#     return
#
#
# func('a')
#
# # 1、封装一个函数greet
# def greet(name):
#     print(f'{name},你好')
#
# # 调用函数
# # 见到了张老师，打一声招呼
# greet('老张')
# # 见到了李老师，打一声招呼
# greet('老李')
# # 见到了王老师，打一声招呼
# greet('老王')



# 1、封装一个函数greet
def greet(name):
   return name + ',你好'

# 调用函数
# 见到了张老师，打一声招呼
print(greet('老张'))
# 见到了李老师，打一声招呼
print("\033[0;31;40m\t" + greet('老李') + "\033[0m")
# 见到了王老师，打一声招呼
print("\033[0;36;40m\t" + greet('老王') + "\033[0m")