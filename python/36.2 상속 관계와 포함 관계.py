class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def __init__(self):
        super().__init__()

    def study(self):
        print('공부하기')

'''
상속 = IS-A 관계
같은 종류에 동등한 관계일 때는 속성을 사용하고,
그 이외에는 속성에 인스턴스를 넣는 방식을 사용한다. 
    (HAS-A 관계)
'''

class Person():
    def greeting(self):
        print('안녕하세요.')

class PersonList: # 전형적인 HAS-A 관계
    def __init__(self):
        self.person_list = []

    def add(self, person):
        self.person_list.append(person)

