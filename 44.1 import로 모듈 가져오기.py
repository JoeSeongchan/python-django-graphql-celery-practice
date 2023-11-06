'''
모듈 = py
패키지 = 특정 기능과 관련한 여러 모듈을 묶은 것
    패키지는 네임스페이스

파이썬 포쥰 라이브러리 = 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를
묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL)이라고 부른다.
'''

'''
import 모듈이름 as 새로운모듈이름

모듈의 일부만 가져오는 방법
    from 모듈이름 import 일부
from 모듈이름 import * 
    로 전부를 가져올 수 있다. 

물론 가져온 모듈을 해제할 수 있다. 
del 모듈이름
'''

import math
del math # import 해제
import math # 재 import
