class Car:
    name='passat'
    price='190000'
    date="2022.1.1"
    def drive(self):
        print("i can run.")


car1 = Car()
print(f"你的第一辆小汽车：{car1.name}")
car1.drive()


car2 = Car()
print(f"你的第二辆小汽车：{car2.name}")
car2.drive()

car3 = Car()
car3.name='benz'
print(f"你的第三辆小汽车：{car3.name}")
car3.drive()

