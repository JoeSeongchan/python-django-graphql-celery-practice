'''
__getitem__ 메서드를 구현하면 인덱스로 접근할 수 있는
이터레이터를 만들 수 있다.
'''

class Counter:
    def __init__(self,stop):
        self.stop=stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

'''
클래스에서 __getitem__ 만 구현해도 이터레이터가 된다.
    __iter__ 나 __next__ 도 생략해도 된다.
'''