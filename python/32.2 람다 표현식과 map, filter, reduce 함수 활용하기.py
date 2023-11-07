'''
람다 표현식에 조건부 표현식 사용하기

3의 배수일 때는 str(x)로 요소를 문자열로 만들어서 반환하고,
    3의 배수가 아닐 때는 그대로 반환하는 코드를 작성해보아라
'''

val_list = [1, 2, 3, 4, 5]
def turn(val):
    if(val%3==0):
        return str(val)
    return val

print(list(map(turn, val_list)))

'''
위 코드를 람다식을 활용한 코드로 바꿔보자! 
'''
print(list(map(lambda x:str(x) if x%3==0 \
               else x,val_list)))

# 람다 표현식 안에 조건문을 넣으면 무조건 else도 같이 넣어야 한다.
# 조건문이 복잡해지면 람다로 하지 말고 함수를 따로 정의해서 넣어라

'''
map에 반복가능한 객체를 여러 개 넣을 수 있다. 
'''
print(list(map(lambda a,b: a+b,[1,2,3],[4,5,6])))

'''
filter를 사용해서 반복 가능한 객체에서 조건에 맞지 않는
    요소를 걸러낼 수 있다. 
'''
def condition(val):
    return val%2==0

print(list(filter(condition,[1,2,3,4,5])))

'''
위 코드를 람다식을 사용해서 표현할 수 있다. 
'''

print(list(filter(lambda x:x%2==0, [1,2,3,4,5])))

'''
reduce 함수를 사용해보자! 
reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
    이전 결과와 누적해서 반환하는 함수이다. 
    Python3 부터는 내장 함수가 아니기 때문에 
        functools에서 가져와야 한다. 
'''

def sum(cur_val, acc):
    return acc+cur_val

from functools import reduce
print(reduce(sum,[1,2,3,4]))

print(reduce(lambda cur_val,acc: cur_val+acc \
             , [1,2,3,4]))

'''
그런데 리스트(딕셔너리, 세트)로 처리할 수 있는 경우에는
    map이나 filter, reduce 보다는 리스트 컴프리헨션
    을 쓰는게 가독성 측면이나 성능 측면이나 더 좋다. 
    
그리고 reduce도 되도록이면 반복문으로 대체하는 게 좋다. 
    가독성 측면에서 더 좋다!
'''



