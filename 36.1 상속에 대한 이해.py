'''
클래스 상속은 연관되면서 동등한 기능일 때 사용한다.
클래스의 상속 관계를 확인하고 싶을 때는 issubclass함수를 사용한다
issubclass(파생클래스,기반클래스) => True
'''

class Person:
    def speak(self):
        print('안녕하세요. 사람입니다.')

class Student(Person):
    def study(self):
        print('안녕하세요. 공부 중입니다.')

issubclass(Student,Person)
