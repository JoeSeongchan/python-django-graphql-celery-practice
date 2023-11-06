def type_check(type1, type2):
    def real_decorator(func):
        def wrapper(a, b):
            if type(a) is not type1 or \
                    type(b) is not type2:
                raise RuntimeError('자료형이 다릅니다.')
            return func(a, b)
        return wrapper
    return real_decorator

'''
if isinstance(a,type_a) and isinstance(b,type_b):
    return func(a,b)
이렇게 쓸 수도 있다. 
'''

@type_check(int, int)
def add(a, b):
    return a + b


print(add(10, 20))
print(add('hello', 'world'))
