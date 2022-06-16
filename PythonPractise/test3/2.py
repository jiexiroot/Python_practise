friends = []
print("欢迎使用好友系统")
print("1：添加好友")
print("2：删除好友")
print("3：备注好友")
print("4：展示好友")
print("5：退出")
while True:
    num = int(input("请输入您的选项："))
    if num == 1:
        add_friend = input("请输入要添加的好友：")
        friends.append(add_friend)
        print('好友添加成功')
    elif num == 2:
        del_friend = input("请输入删除好友姓名：")
        friends.remove(del_friend)
        print("删除成功")
    elif num == 3:
        before_friend = input("请输入要修改的好友姓名：")
        after_friend = input("请输入修改后的好友姓名：")
        friend_index = friends.index(before_friend)
        friends[friend_index] = after_friend
        print("备注成功")
    elif num == 4:
        if len(friends) == 0:
            print("好友列表为空")
        else:
            for i in friends:
               print(i)
    elif num == 5:
        break
