'''
파이썬에서는 함수 안에서 함수를 정의할 수 있다.
'''
def print_hello():
    hello = "Hello, world!"
    def print_message():
        print(hello)
    print_message()

'''
안쪽 함수에서 바깥쪽 함수의 지역 변수를 참조할 수 있다. 
안쪽 함수에서 바깥쪽 함수의 지역 변수 값을 변경하려면 nonlocal 키워드를 사용해야 한다. 
'''

def A():
    x = 10
    def B():
        nonlocal x # 현재 함수의 지역변수가 아니라는 뜻
        x = 20
    B()
    print(x)

A()

'''
nonlocal은 원 함수와 가장 가까운 계층의 함수의 지역변수들
부터 뒤진다.
사실 계층 구조를 복잡하게 하면서 프로그래밍할 일은 거의 없다.
있더라도 변수 명을 다 다르게 해서 명확하게 다른 변수임을 표시한다.
'''

'''
함수가 몇 단계든 상관 없이 global 키워드를 사용하면 무조건 전역 변수를 
사용하게 된다. 

값을 주고 받을 때는 매개변수와 반환값을 이용하는 게 좋다.
왜냐하면 부수효과를 파악하기 힘들기 때문이다. 
'''
