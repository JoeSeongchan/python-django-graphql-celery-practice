'''
파이썬은 데코레이터 (decorator)라는 기능을 제공
@ 로 시작하는 것들이 데토레이터이다.
    함수를 장식한다고 해서 이런 이름이 붙었다.
    디자인 패턴 중에서 데코레이터 패턴과 메커니즘이 비슷하다.
'''

class Calc:
    @staticmethod # 데코레이터
    def add(a,b):
        print(a+b)

'''
데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용한다. 
Spring의 AOP와 비슷해보이기도 한다. 

함수의 시작과 끝을 출력하는 데코레이터를 만들어보자
'''
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()
'''
데코레이터는 호출할 함수를 매개변수로 받는다. 
데코레이터 안에서 호출할 함수를 감싸는 wrapper를 만든다. 
데코레이터는 wrapper 함수 자체를 반환한다.
함수 안에서 함수를 만들고 반환하는 클로저이다. 

@를 사용해서 좀 더 간편하게 데코레이터를 사용해보자!
'''
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
world()

'''
데코레이터는 함수를 감싸는 형태로 구성되어 있다. 
그래서 데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용한다. 

여러 개의 데코레이터를 하나의 함수에 지정할 수 있다.
위에서 아래 순서대로 데코레이터가 적용된다. 
'''

def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

'''
위 코드는 아래 코드와 동일한 코드이다.

decorated_hello = decorator1(decorator2(hello))
decorated_hello()
'''
