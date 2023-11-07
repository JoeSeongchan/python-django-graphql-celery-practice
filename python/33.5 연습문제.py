'''
C, C++의 static 로컬 변수를 클로저로 구현할 수 있다.

복습

클로저 : 함수를 둘러싼 환경을 유지하다가 나중에 사용하는 함수
'''
def counter():
    i = 0
    def count():
        nonlocal i
        i+=1
        return i
    return count

c = counter()
for i in range(10):
    print(c(),end=' ')
