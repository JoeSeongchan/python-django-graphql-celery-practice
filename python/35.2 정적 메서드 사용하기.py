'''
정적 메서드와 클래스 메서드는 다른 개념이다!

정적 메서드
메서드 위에 @staticmethod를 붙인다.
매개변수에 self를 지정하지 않아도 된다.
'''

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20)
Calc.mul(10,20)

'''
정적 메서드에서는 인스턴스 속성이나 인스턴스 메서드에 접근할 수 없다.
    self 파라미터가 없기 때문이다. 

정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들 때 사용한다. 
    순수함수란? 
        부수 효과가 없고 입력 값이 같으면 언제나 같은 출력 값을 반환하는 함수
'''
