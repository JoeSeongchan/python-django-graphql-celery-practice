'''
매개변수가 있는 데코레이터를 만드는 방법
매개변수로 값을 전달해서 다른 동작을 수행하게 만들 수 있다.

함수의 반환 값이 특정 수의 배수인지 확인하는 데코레이터
'''
def is_multiple(x): # 데코레이터가 사용할 매개변수 지정
    def real_decorator(func): # 호출할 함수를 매개변수로 받음
        def wrapper(a,b): # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a,b)
            if r % x == 0:
                print('배수이다')
            else:
                print('배수가 아닙니다')
            return r
        return wrapper
    return real_decorator

@is_multiple(3)
def add(a,b):
    return a+b

print(add(10,20))
print(add(2,5))

'''
@functools.wraps(func) 
이걸 wrapper에 붙인다. 
원래 함수의 정보를 유지시켜준다. 
    디버깅을 할 때 유용하므로 데코레이터를 만들 때는 
    @functools.wraps를 사용하는 게 좋다. 
'''