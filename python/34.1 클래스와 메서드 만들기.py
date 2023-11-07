'''
클래스 안에 있는 데이터를 속성이라고 부르고,
    클래스 안에 있는 기능을 메서드라고 부른다.
파이썬에서는 모든 것이 객체이다!

메서드의 첫번째 매개변수는 반드시 self이다.

인스턴스를 통해 호출하는 메서드를 인스턴스 메서드라고 한다.

int, list, dict도 사실 클래스이다.
'''

c = dict(x=10,y=20)

'''
파이썬에서는 자료형도 클래스이다. 
type(...) 메서드를 통해서 객체가 어떤 클래스의 인스턴스인지 알 수 있다. 
'''

'''
내용이 없는 빈 클래스를 만들 때는 pass를 넣는다. 
'''
class Person:
    pass

'''
특정 객체가 특정 클래스의 인스턴스인지 확인할 때는 
isinstance 메서드를 사용한다. 
isinstance(객체,클래스)
'''

def factorial(n):
    if not isinstance(n, int) or n<0:
        return None
    if n == 1:
        return 1
    return n*factorial(n-1)
