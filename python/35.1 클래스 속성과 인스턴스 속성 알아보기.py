'''
속성에는 두 가지 종류가 있다.
    - 인스턴스 속성
        __init__ 안에서 만들었던 속성이 인스턴스 속성이다.
    - 클래스 속성
        인스턴스가 아닌 클래스에 속한 속성이다.
        모든 인스턴스가 공유한다.

클래스 속성에 접근할 때는 클래스 이름을 사용한다.

---
파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾는다.
인스턴스와 클래스에서 __dict__를 출력해보면 인스턴스와 클래스의 속성을 찾을 수 있다.

인스턴스 메서드는 인스턴스.__dict__에 표시되지 않는다.
인스턴스 메서드는 클래스.__dict__에 표시된다.
'''

'''
함수와 마찬가지로 클래스와 메서드에도 독스트링을 사용할 수 있다. 
class 나, def 바로 밑에 """으로 적으면 된다. 

클래스.__doc__, 클래스.메서드.__doc__으로 참조할 수 있다. 
'''