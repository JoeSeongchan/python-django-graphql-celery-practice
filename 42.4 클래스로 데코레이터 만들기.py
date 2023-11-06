'''
클래스로 데코레이터를 만드는 방법
인스턴스를 함수처럼 호출하게 해주는 __call__ 메서드를 구현해야 한다.
'''

class Trace:
    def __init__(self,func): # 호출할 함수를 초깃값으로 받는다.
        self.func = func # 속성으로 저장한다.

    def __call__(self):
        print(self.func.__name__,'함수 시작')
        self.func()
        print(self.func.__name__,'함수 끝')

@Trace
def hello():
    print('hello')

hello()

def hello():
    print('hello')

trace_hello = Trace(hello)
trace_hello()
'''
이런식으로 데코레이터를 적용할 수도 있다. 
'''
