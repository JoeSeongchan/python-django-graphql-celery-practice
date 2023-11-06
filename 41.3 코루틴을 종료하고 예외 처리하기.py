'''
보통은 코루틴은 실행 상태를 유지하기 위해서 while True:
로 계속 반복한다. 코루틴을 강제종료하고 싶으면 close 메서드를
호출한다.
코루틴객체.close()
'''

def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')

co = number_coroutine()
next(co) # 코루틴을 시작하기 위해서는 처음에 next를 호출해야 한다.

for i in range(20):
    co.send(i)

co.close() # 코루틴 종료

'''
사실 코루틴은 스크립트가 종료되면 같이 종료된다.

코루틴이 close로 종료되면 GeneratorExit 예외가 발생한다.
이 GeneratorExit 예외를 코루틴 안에서 처리하면 
코루틴 안에서 자기 자신의 종료를 깨닫고 작업을 처리할 수 있다. 
'''
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x,end=' ')
    except GeneratorExit:
        print()
        print('코루틴 종료')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()

'''
코루틴 안에서 예외를 발생시키고 싶다면 메인 루틴에서 코루틴객체.throw(예외이름,에러메시지)
를 호출한다. 
'''

def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total # throw 메소드의 반환 값으로 사용된다.

co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError,'예외로 코루틴 끝내기'))
