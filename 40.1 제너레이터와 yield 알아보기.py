'''
제너레이터 = 이터레이터를 생성해주는 함수
이터레이터는 클래스 안에 __iter__, __next__ 또는 __getitem__
메서드를 구현해야 하지만 제너레이터는 함수 안에 yield 키워드만
넣으면 된다.

제너레이터 = 발생자
yield 키워드가 들어 있는 함수 = 제너레이터 생성 함수
함수를 호출하면 반환되는 객체 = 제너레이터
    제너레이터는 __iter__ , __next__ 를 가지고 있다.
    yield에 지정한 값이 __next__메서드의 반환 값으로 나온다
    제너레이터는 함수의 끝까지 도달하면 StopIteration 예외가
    자동으로 발생한다.
    제너레이터 객체에서 __iter__를 호출하면 self를 반환한다.
    yield = 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에
    양보한다.
    제너레이터 안에서 return 에 반환 값을 지정하면 StopIteration
    예외의 에러 메시지로 들어간다.
'''

def number_generator():
    yield 0
    yield 1
    yield 2

# __iter__를 호출해서 이터레이터를 구한다.
# 이터레이터의 __next__ 메서드를 반복해서 호출한다.
#   StopIteration 에러가 발생했을 때까지 반복
for i in number_generator():
    print(i)