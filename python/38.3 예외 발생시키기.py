try:
    x = int(input('3의 배수를 입력하세요: '))
    if x%3 !=0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)
except Exception as e:
    print("예외가 발생했습니다.",e)
'''
Exception이 아니라 RuntimeError 또는 NotImplementedError
를 사용해도 된다. 
'''

def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x%3 !=0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)

try:
    three_multiple() # 함수 안에서 발생한 예외를 밖에서 해결
except Exception as e:
    print('예외가 발생했습니다.',e)


# 현재 예외를 다시 발생시키는 법
# except 안에서 raise를 사용하면 현재 예외를 다시 발생시킨다.
# re-raise
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x%3 !=0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.',e)
        raise # 예외를 다시 발생시켜서 상위 코드 블럭으로 넘긴다.
        # raise RuntimeError('다른 예외 발생')
'''
assert를 사용해서 꼭 만족해야 하는 조건을 체크할 수 있다.
assert x%3 == 0, '3의 배수가 아닙니다.'
만약 조건을 만족하지 못한다면 AssertionError가 발생한다.
이는 debug 모드일 때만 활성화된다.
파이썬은 기본적으로 debug 모드이지만 python -O XXX.py 로
스크립트 파일을 실행하면 debug 모드가 해제된다. 
'''

try:
    three_multiple()
except Exception as e:
    print('스크립트 파일에서 예외가 발생했습니다.',e)