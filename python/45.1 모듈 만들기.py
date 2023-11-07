class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.\
              format(self.name))

maria = Person('마리아',20,'서울시 서초구 반포동')
maria.greeting()


