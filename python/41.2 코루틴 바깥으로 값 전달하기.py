'''
변수 = (yield 변수)
변수 = next(코루틴 객체)
변수 = 코루틴 객체.send(값)
'''
def sum_coroutine():
    total = 0
    while True:
        # x : 외부에서 전달 받은 값
        # total : 외부에 전달할 값
        x = (yield total)
        total += x

co = sum_coroutine()
print(next(co)) # total 값을 가져온다.
# yield에서 total을 메인 루틴으로 전달하고 대기한다.

print(co.send(1)) # 1을 보내고 코루틴에서 나온 값 출력

'''
제너레이터와 코루틴의 차이점 
제너레이터 : next 함수를 반복 호출하여 값을 얻어내는 방식
코루틴 : next 함수를 한 번만 호출한 뒤, send로 값을 주고 받는 방식

값을 보내지 않으면서 코루틴의 코드를 실행할 때는 next함수만 호출하면 된다.
이렇게 되면 제너레이터처럼 동작한다. 
'''
