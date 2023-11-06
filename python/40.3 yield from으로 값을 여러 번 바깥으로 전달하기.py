'''
어떻게 하면 값을 여러 번 바깥으로 전달할 수 있을까?
'''
def number_generator():
    x = [1,2,3]
    for i in x:
        yield i

for i in number_generator():
    print(i)

# 이런 경우에 yield from을 이용하면 된다.
# yield from에는 반복 가능한 객체, 이터레이터, 제너레이터 객체
# 를 지정한다.

def number_generator():
    x = [1,2,3]
    yield from x

for i in number_generator():
    print(i)

# yield from에 제너레이터 객체 지정하기
def number_generator(stop):
    n = 0
    while n<stop:
        yield n
        n+=1

def three_generator():
    yield from number_generator(3)

for i in three_generator():
    print(i)

'''
파이썬 고급 기능에 해당하는 부분이라 이해하기 쉽지 않다. 
리스트 표현식을 사용할 때 대괄호를 사용했다. 
같은 리스트 표현식을 괄호로 묶으로 제너레이터 표현식이 된다.
리스트 표현식 = 처음부터 리스트의 요소를 만들어낸다.
제너레이터 표현식 = 필요할 때 요소를 만들어낸다. 
'''
[i for i in range(50) if i%2 == 0] # 리스트를 만든다

(i for i in range(50) if i%2 == 0) # generator를 만든다