class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        if self.score >= 90:
            return f'{self.name},{self.score}分,成绩优秀'
        elif self.score >= 80:
            return f'{self.name},{self.score}分,成绩良好'
        elif self.score >= 70:
            return f'{self.name},{self.score}分,成绩中等'
        elif self.score >= 60:
            return f'{self.name},{self.score}分,成绩合格'
        else:
            return f'{self.name},{self.score}分,成绩不合格'


p1 = student('Tom', 85)
print(p1)

p2 = student('Jack', 65)
print(p2)
