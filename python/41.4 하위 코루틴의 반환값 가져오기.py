def accumulate():
    total = 0
    while True:
        x = (yield) # 상위 루틴에서 값을 받는다
        if x is None:
            return total # None을 받으면 total을 리턴한다
            # 코루틴을 끝낸다
        total += x # 계속 더한다

def sum_coroutine():
    while True:
        total = yield from accumulate()
        '''
        상위 루틴에서 값을 받아서 accumulate에 계속 전달한다. 
        accumulate는 계속 값을 받는다
        accumulate에 None이 전달되면 그 때 accumulate 코루틴이 종료된다. 
        상위 루틴에서 받은 값을 하위 루틴에 그대로 전달할 때 yield from 키워드를 사용한다.
        '''
        # yield from = 코루틴의 반환 값을 가져온다.
        print(total) # total을 출력한다

co = sum_coroutine() # 코루틴 객체를 만든다.
# 코루틴에서 yield from을 사용하면 코루틴 바깥에서 send로 하위 코루틴까지 값을 보낼 수 있다

next(co)

for i in range(1,11):
    co.send(i) # 코루틴 accumulate에 숫자를 보낸다.

# 누적을 끝내고 싶으면 None을 보낸다.
'''
Python 3.6까지는 raise StopIteration(값) 으로 상위 루틴에 값을 전달했다.
그런데 Python 3.7 부터는 StopIteration이 RuntimeError로 바뀌기 때문에
return 키워드를 사용해야 한다. 
'''

'''
코루틴은 함수가 종료되지 않은 상태에서 값을 주고 받을 수 있는 함수이다. 
    현재 코드의 실행을 대기하고 상대방의 코드를 실행한다. 
    코루틴은 시간이 오래 걸리는 작업을 분할하여 처리할 때 주로 사용한다.
        파일 처리, 네트워크 처리
'''

def number_coroutine():
    x = None
    while True:
        x = (yield x) # x를 밖으로 보내고, x를 받아온다
        if x == 3:
            return x # x가 3이면 코루틴을 종료하고 상위 루틴에 값을 전달한다

def print_coroutine():
    while True:
        x = yield from number_coroutine() # 상위 루틴에게서 받은 값을 하위 루틴에 전달한다.
        # 하위 루틴에서 받은 값을 상위 루틴에게 전달한다.
        print('print_coroutine: ',x)

co = print_coroutine()
next(co)

x = co.send(1)
print(x)
x = co.send(2)
print(x)
co.send(3)

# 이터레이터, 제너레이터, 코루틴 개념이 조금 어렵긴 하다.
# 하지만 계속 연습하고 숙달하여 마스터하자!