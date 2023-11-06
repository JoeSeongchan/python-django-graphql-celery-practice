'''
매개변수와 반환값을 처리하는 데코레이터를 만들어보자
'''

def trace(func):
    def wrapper(a, b):
        r = func(a,b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__,a,b,r))
        return r
    return wrapper

@trace
def add(a,b):
    return a+b

print(add(10,20))

'''
가변 인수 함수 데코레이터
'''
def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__,args,kwargs,r))
        return r
    return wrapper

@trace
def get_max(*args):
    return max(args)

@trace
def get_min(**kwargs):
    return min(kwargs.values())

print(get_max(10,20))
print(get_min(x=10,y=20,z=30))

'''
위치인수와 키워드 인수를 모두 받을 수 있도록
*args, **kwargs 를 쓴다. 

args = 튜플
kwargs = 딕셔너리
'''
def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'
              .format(func.__name__,args,kwargs,r))

        return r
    return wrapper

@trace
def add(a,b):
    return a+b

'''
메서드에 데코레이터를 만들 때는 self를 주의해야 한다. 
인스턴스 메서드는 항상 self를 받으므로 데코레이터를 만들 때도
wrapper 함수의 첫번째 매개변수는 항상 self로 지정해야 한다. 
* 클래스 메서드는 cls를 항상 가진다. 
'''

def trace(func):
    def wrapper(self,a,b):
        r = func(self,a,b)
        print('{0}(a={1},b={2})->{3}'
              .format(func.__name__,
                      a,b,r))
        return r
    return wrapper

class Calc:
    @trace
    def add(self,a,b):
        return a+b

c = Calc()
print(c.add(10,20))
