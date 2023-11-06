def find(keyword:str):
    is_contained = False
    while True:
        sentence:str = (yield is_contained)
        is_contained = keyword in sentence

f = find('Python')
next(f)

print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))

# 이터레이터, 제너레이터, 예외처리, 코루틴 총정리
# https://dojang.io/mod/page/view.php?id=2425

