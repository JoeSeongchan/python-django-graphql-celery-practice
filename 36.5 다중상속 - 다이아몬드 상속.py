# 죽음의 다이아몬드
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C):
    pass

x = D()
x.greeting() # 어느 클래스의 greeting이 호출될까?
# B, C 순서대로 상속하니 B에서 먼저 greeting을 찾아 호출한다.
# mro = method resolution order (메서드 탐색 순서)를 따른다.
