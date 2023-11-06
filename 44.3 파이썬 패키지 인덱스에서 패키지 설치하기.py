'''
Python Standard Library (PSL) 외에 다른 패키지를 설치해야
할 일이 있다. 그런 경우 Python Package Index를 사용한다.
PyPI

명령만 입력하면 원하는 패키지를 인터넷에서 다운로드하여 설치한다.
'''

'''
python -m pip install XXX
pip install XXX

python3 의 경우
python3 -m pip install XXX
pip3 install XXX
'''

'''
pip search 패키지 : 패키지 검색 
pip install 패키지==버전 : 특정 버전의 패키지를 설치
pip list 또는 pip freeze : 패키지 목록 출력 
pip uninstall 패키지 : 패키지 삭제 

pip freeze > requirements.txt
    현재 설치되어 있는 패키지 목록을 requirements.txt에 기록한다.
    
pip install -r requirements.txt
    requirements.txt 안에 적힌 패키지 목록을 설치한다. 
'''

