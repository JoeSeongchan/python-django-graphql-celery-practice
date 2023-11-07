'''
모듈은 스크립트 파일이 한 개지만 패키지는 폴더(디렉토리)로 구성되어 있다.
폴더 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식한다.
파이썬 3.3 이상부터는 없어도 되지만 하위 버전 호환성을 위해서 기본적으로 __init__.py는 넣는 편이다.

패키지의 모듈에서는 __name__ 변수에 `패키지.모듈`이 들어간다.

파이썬은 현재 폴더에 모듈과 패키지가 없으면 미리 설정된 경로에서 모듈과 패키지를 찾는다.
sys.path에는 모듈, 패키지를 찾는 경로가 들어있다.
site-packages 폴더에는 pip로 설치한 패키지가 들어간다.
자기가 만든 모듈 패키지도 넣을 수 있다.

만약 venv를 쓰고 있다면 venv/Lib/site-packages 안에 pip로 설치한
라이브러리의 패키지, 모듈이 들어간다.
'''

class Person:

    def __init__(self,name:str,gender:str,height:str,local:str):
        self.name = name
        self.gender = gender
        self.height = height
        self.local = local



