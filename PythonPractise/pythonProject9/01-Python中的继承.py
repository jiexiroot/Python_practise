class Person(object):
    def eat(self):
        print('i can eat food!')

    def speak(self):
        print('i can speak!')


class Teacher(Person):
    pass


class Student(Person):
    pass


teacher = Teacher()
teacher.eat()
teacher.speak()

student = Student()
student.eat()
student.speak()