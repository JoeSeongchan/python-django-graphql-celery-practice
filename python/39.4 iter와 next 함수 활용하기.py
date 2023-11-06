'''
여기서 말하는 iter, next 함수는 __iter__, __next__ 함수가
아니다. 파이썬 내장 함수 iter, next 함수를 말하는 것이다.

iter는 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝낸다.
iter(호출 가능한 객체, 반복을 끝낼 값)
    호출 가능한 객체 = callable
    반복을 끝낼 값 = sentinel (감시병이라는 뜻)
'''
import random
it = iter(lambda: random.randint(0,5), 2)
# 이렇게 iter 함수를 활용하면 if 조건문으로 매번 조건을 체크하지 않아도 되니 좋다.

'''
next에는 기본값을 지정할 수 있다.
next(반복 가능한 객체, 기본 값)
    반복이 끝났을 때는 기본 값을 리턴한다. 
'''
it = iter(range(3))
next(it,10)
next(it,10)