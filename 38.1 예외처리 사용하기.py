try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10/x
    print(y)
except:
    print('예외가 발생했습니다.')

y = [10,20,30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index]/x)
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.',e)
except IndexError as e:
    print('잘못된 인덱스입니다.',e)

'''
예외가 여러 개 발생하면 먼저 발생한 예외의 처리 코드가 먼저 실행

기반 예외 클래스가 파생 예외 클래스보다 먼저 처리
'''