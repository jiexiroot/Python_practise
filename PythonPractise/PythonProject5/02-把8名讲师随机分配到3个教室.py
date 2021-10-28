import random

rooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for teacher in teachers:
    # 3、生成随机数
    index = random.randint(0, 2)
    rooms[index].append(teacher)

i = 1
for room in rooms:
    print(f'第{i}个教室中的讲师：{room}')

# 第一间教室
rooms[0]
# 第二间教室
rooms[1]
# 第三间教室
rooms[2]
