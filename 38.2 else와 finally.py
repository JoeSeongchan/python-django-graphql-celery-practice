try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10/x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)
finally:
    print('코드 실행이 끝났습니다.')

'''
try 안에서 만든 변수는 try 바깥에서 사용할 수 있다.
try는 함수가 아니므로 스택 프레임을 만들지 않는다.
try 안에서 변수를 만들더라도 try 바깥에서 사용할 수 있다. 
'''