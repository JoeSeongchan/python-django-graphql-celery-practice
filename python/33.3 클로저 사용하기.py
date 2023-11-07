'''
함수 안에서 함수를 정의하고 그 함수를 리턴하면
    리턴 받은 함수는 클로저가 된다.
'''
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a*x+b
    return mul_add

c = calc() # 클로저를 리턴 받았다.
print(c(1),c(2),c(3),c(4))

'''
함수를 둘러싼 환경 (지역 변수, 코드 등)을 계속 유지하다가,
    함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저라고 한다.
클로저를 사용하면 프로그램의 흐름을 변수에 저장할 수 있다.
클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용한다.
또한 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로
    데이터를 숨기고 싶을 때 활용한다. 
'''

'''
lambda 로도 클로저를 만들 수 있다. 
'''

def calc():
    a = 3
    b = 5
    return lambda x: a*x+b

c = calc()
print(c(4))

'''
lambda와 closure를 혼동하는 경우가 많다.
closure : 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수
lambda : 익명 함수를 편하게 사용하는 양식
'''

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total # 바깥 함수의 지역 변수 값을 변경하고 싶을 때 사용한다.
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)
c(2)
