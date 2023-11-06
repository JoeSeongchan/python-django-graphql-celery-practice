def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline() # 한 줄씩 읽어야 한다
            if line == '':
                break
            yield line.strip('\n') # 파일에서 읽은 \n은 출력하지 않아야 한다.

'''
용량이 매우 큰 파일은 메모리에 한꺼번에 읽어서 처리하기 힘들다
대용량 데이터를 부분부분 처리해야 할 때 이렇게 제너레이터를 활용한다.
'''
for i in file_read():
    print(i)