from calcpkg45_4 import *
print(add(1,2))

'''
__all__로 필요한 것만 공개할 수 있다. 
__init__.py 안에 다음 코드를 넣는다. 

__all__ = ['add', 'triangle_area']    # calcpkg 패키지에서 add, triangle_area 함수만 공개
__all__ 안에 들어 있는 식별자만 사용할 수 있다. 

파이썬은 하위 패키지를 만들 수 있다. 
하위 패키지 안에 있는 모든 함수, 변수를 가져오고 싶다면 
아래와 같이 하면 된다. 
from .operation.element import *
from .operation.logic import *
from .geometry.shape import *
from .geometry.vector import *
'''

'''
독스트링 

모듈의 독스트링은 모듈 파일의 첫 줄에 작은따옴표 세 개를 사용하여 넣는다.
패키지의 독스트링은 __init__.py에 넣는다. 

모듈과 패키지의 독스트링을 출력하려면 모듈 또는 패키지의 __doc__을 출력하며 된다. 
모듈.__doc__
패키지.__doc__
'''

