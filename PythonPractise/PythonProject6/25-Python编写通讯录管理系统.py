# 1、封装一个menu函数，专门用于打印选择界面菜单
def menu():
    print('-' * 40)
    print('杰希教育通讯录管理系统V1.0')
    print('1、添加学员信息')
    print('2、删除学员信息')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、遍历学员信息')
    print('6、退出系统')
    print('-' * 40)


# 6、定义一个全局遍历
info = []


# 5、定义add_student方法，用于添加学员信息
def add_student():
    # 定义一个空字典，接收name,age,mobile
    info_dict = {}
    # 提示用户输入学员信息name,age,mobile
    info_dict['name'] = input('请输入学员姓名：')
    info_dict['age'] = input('请输入学员年龄：')
    info_dict['mobile'] = input('请输入学员电话：')
    # 声明全局变量info
    global info
    # 追加数据到info列表中
    info.append(info_dict)
    print('学员信息添加成功！')


# 7、定义del_student方法
def del_student():
    # 提示用户输入要删除学员的信息
    name = input('请输入您要删除学员的姓名：')
    global info
    # 判断name是否存在于info的字典里
    for i in info:
        if i['name'] == name:
            # 查找到了学员信息
            info.remove(i)
            print('学员信息删除成功')
            break
    else:
        # 未找到学员信息
        print('暂未查询到您要删除的学员信息')


# 8、定义modify_student()方法,用于修改学员信息
def modify_student():
    # 提示用户输入要修改学员的信息
    name = input('请输入您要修改学员的姓名：')
    global info
    # 判断name是否存在于info的字典里
    for i in info:
        if i['name'] == name:
            # 查找到了学员信息
            i['name'] = input('请输入修改后的姓名：')
            i['age'] = input('请输入修改后的年龄：')
            i['mobile'] = input('请输入修改后的电话：')
            print('学员信息修改成功')
            break
    else:
        # 未找到学员信息
        print('暂未查询到您要修改的学员信息')


# 9、定义select_student()方法，用于查询某个学员信息
def select_student():
    # 提示用户输入要查询学员的信息
    name = input('请输入您要查询学员的姓名：')
    # 循环遍历，判断name是否存在
    for i in info:
        if i['name'] == name:
            # 查询到了学员信息
            print(f'学员姓名：{i["name"]},学员年龄：{i["age"]},学员电话：{i["mobile"]}')
            break
    else:
        # 未找到学员信息
        print('暂未查询到您要查询的学员信息')


# 10、定义select_all()方法，用于遍历所有学员信息
def select_all():
    # 直接对info进行遍历操作
    for i in info:
        print(f'学员姓名：{i["name"]},学员年龄：{i["age"]},学员电话：{i["mobile"]}')


# 4、编写死循环，让程序可以一直执行下去
while True:
    menu()
    # 2、使用input方法接收用户的输入信息
    user_num = int(input('请输入您要操作的功能序号：'))

    # 3、使用if多分支条件实现不同的功能

    if user_num == 1:
        # 添加学员信息
        add_student()
    elif user_num == 2:
        # 删除学员信息
        del_student()
    elif user_num == 3:
        # 修改学员信息
        modify_student()
        pass
    elif user_num == 4:
        # 查询学员信息
        select_student()
        pass
    elif user_num == 5:
        # 遍历所有学员信息
        select_all()
        pass
    elif user_num == 6:
        # 退出系统
        print('感谢您使用杰希教育通讯录管理系统V1.0')
        break
    else:
        print('信息输入错误，请重新输入.....')
