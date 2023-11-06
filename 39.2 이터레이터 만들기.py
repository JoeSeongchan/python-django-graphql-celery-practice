class Counter: # 이터레이터를 정의했다
    # 반복 가능한 객체(iterable)이면서 이터레이터(iterator)이다.
    def __init__(self,stop):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current+=1
            return r
        else:
            raise StopIteration

for i in Counter(3):
    print(i, end=' ')

'''
이터레이터는 언패킹이 가능하다. 
이터레이터의 결과를 변수 여러 개에 할당할 수 있다.
물론 이터레이터가 반복하는 횟수와 변수의 개수는 같아야 한다. 
우리가 자주 사용하는 map도 이터레이터이다. 
그래서 언패팅으로 변수 여러 개에 값을 할당할 수 있다. 
    map 함수의 리턴 값은 이터레이터이다. 
'''

'''
반환값을 _ 라는 이름의 변수에 저장하는 이유 
    반환 값을 사용하지 않고 무시하겠다는 관례적 표현이다. 
'''

a, b, c = Counter(3) # 이터레이터는 언패킹하여 여러 변수에 값을 넣을 수 있다.

