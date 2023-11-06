'''
클래스로 만든 데코레이터도 매개변수와 반환값을 처리할 수 있다.
'''

class Trace:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 받은 매개변수들을 self.func에 넣을 때는
        # 언패킹해서 넣는다.
        r = self.func(*args, **kwargs)
        return r

@Trace
def add(a,b):
    return a+b

print(add(10,20))
print(add(a=10,b=20))

# ---
# 클래스로 매개변수가 있는 데코레이터 만들기
class IsMultiple:
    def __init__(self,x):
        self.x = x

    def __call__(self, func):
        def wrapper(a,b):
            r = func(a,b)
            if r % self.x == 0:
                print('배수입니다.')
            else:
                print('배수가 아닙니다.')
            return r
        return wrapper

@IsMultiple(3)
def add(a,b):
    return a+b

print(add(10,20))

'''
가장 중요한 것 
데코레이터 = 기존 함수를 수정하지 않으면서 추가 기능을 구현할 
    때 사용하는 것

주로 디버깅, 함수의 성능 측정, 실행 전 데이터 확인 등에 사용한다. 
'''
