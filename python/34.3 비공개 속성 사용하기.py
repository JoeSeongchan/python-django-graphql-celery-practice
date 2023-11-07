'''
클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수
    있는 비공개 속성을 어떻게 선언하고 정의할까?
비공개 속성은 이름이 밑줄 2개로 시작해야 한다.
    단 뒤에 밑줄이 2개 더 추가되면 비공개 속성이 아니다.
'''

class Person:
    __slots__ = ['name','age','address','__wallet']
    def __init__(self,name,age,address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

# 캡슐화를 할 수 있다! 외부에서 내부 데이터에 함부로 접근하지 못하게 한다.

'''
비공개 메서드도 정의할 수 있다. 
비공개 메서드는 이름의 앞에 밑줄 두 개 붙어야 한다. 
'''

class Person:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()


james = Person()
james.__greeting() # 접근할 수 없다!
