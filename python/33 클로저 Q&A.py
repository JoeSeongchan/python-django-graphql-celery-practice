'''
일급 객체는 다음 조건을 만족하는 객체를 말한다.
    - 변수나 데이터 구조에 넣을 수 있어야 한다.
    - 매개변수에 전달할 수 있어야 한다.
    - 반환 값으로 사용할 수 있어야 한다.
일급 함수는 '일급 객체의 조건을 만족하면서 실행 중에 함수를 생성할 수 있어야 한다.'
def 안에 def 를 만들거나 람다를 통해서 runtime에 함수를 생성할 수 있으므로
    파이썬의 함수는 일급 함수이다.

---
파이썬에는 switch 문법이 없지만 딕셔너리와 람다 표현식을 사용해서 비슷하게
    구현할 수 있다.
'''
switch = {
    '+' : lambda x,y: x+y ,
    '-' : lambda x,y: x*y
}
x = '+'
try:
    print(switch[x](10,20))
except KeyError:
    print('default')