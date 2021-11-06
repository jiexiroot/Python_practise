class XiaoMing():
    def __init__(self, weight):
        self.name = '小明'
        self.weight = weight

    def __str__(self):
        return f'当前{self.name}的体重为{self.weight}公斤'

    # 吃东西
    def eating(self):
        self.weight += 1
        print('小明又吃东西了，胖了1公斤！')

    # 减肥
    def exercise(self):
        self.weight -= 1
        print('小明减肥了0.5公斤了！')


xiaoming = XiaoMing(75)
xiaoming.eating()
xiaoming.exercise()
xiaoming.exercise()
xiaoming.exercise()
xiaoming.exercise()
xiaoming.exercise()
xiaoming.exercise()
print(xiaoming)