class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        super().__init__() # 이게 없으면 기반 클래스의 속성을 사용할 수가 없다.
        # super(Student,self).__init__() 와 같은 기능을 한다.
        print('Sutdent __init__')
        self.school = '파이썬 코딩 도장'

'''
만약 파생 클래스의 생성자를 따로 정의하지 않았다면 
super().__init__()를 명시적으로 호출하지 않아도 된다.
알아서 호출해주기 때문이다.
'''

james = Student()
print(james.school)
print(james.hello)
