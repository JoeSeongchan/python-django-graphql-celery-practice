'''
프로그래머가 직접 만든 예외를 사용자 정의 예외라고 부른다.
Exception을 상속받아서 새로운 클래스를 만든다.
기반 클래스의 생성자 파라미터로 예외 메시지를 넘긴다.
'''
class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

'''
물론 새로운 예외를 정의할 때 생성자를 명시적으로 정의하지 않아도 
된다. 
class NotThreeMultipleError(Exception):
    pass
로 코드를 작성해도 된다.
단, 이 때는 raise NotThreeMultipleError 가 아니라
raise NotThreeMultipleError('에러 메시지') 를 써야 한다. 
'''

def three_multiple():
    try:
        x=int(input('3의 배수를 입력하세요: '))
        if x%3!=0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.',e)

three_multiple()