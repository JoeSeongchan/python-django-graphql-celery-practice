def number_generator(stop):
    n = 0
    while n<stop:
        yield n
        n+=1

for i in number_generator(3):
    print(i)

# yield 는 값을 생성함과 동시에 실행 흐름을 바깥으로 양보한다.
# 여기에서 바깥은 Caller이다.
# 값을 Caller에게 전달한다.
#   Caller가 __next__를 호출했을 텐데 이 호출 결과로 리턴한다.
