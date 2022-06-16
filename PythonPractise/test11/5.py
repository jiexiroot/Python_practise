class score:
    name = ''
    c = 0
    java = 0
    english = 0
    math = 0
    sum = 0

    def __str__(self):
        return self.name + '：c# :' + str(self.c) +'java: ' + str(self.java) + '英语: ' + str(self.english) + '数学: ' + str(self.math) + '总分: ' + str(self.sum)

    def __init__(self, name, c, java, english, math):
        self.name = name
        self.c = c
        self.java = java
        self.english = english
        self.math = math

    def total(self):
        sum = self.c + self.java + self.english + self.math
        self.sum = sum

    def prtscore(self):
        print(f'姓名：{self.name} C#:{self.c}JAVA#:{self.java}英语{self.english}数学:{self.math}\n总分{self.sum}')

score1 = score('李明', 65, 72, 36, 86)
score2 = score('王兵', 81, 70, 65, 71)
score3 = score('刘萍', 73, 64, 88, 65)
clist = []
clist.append(score1)
clist.append(score2)
clist.append(score3)
for i in range(len(clist)):
    clist[i].total()
    print(clist[i])

list2 = [str((clist[i])) for i in range(len(clist))]

print(list2)
for i in range(len(clist)):
    clist[i].prtscore()
