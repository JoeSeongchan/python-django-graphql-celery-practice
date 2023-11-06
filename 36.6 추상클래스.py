from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def 메서드1(self):
        pass

    @abstractmethod
    def 메서드2(self):
        pass

class Student(StudentBase):
    def 메서드1(self):
        pass

    def 메서드2(self):
        pass

james = Student()
james.메서드1()
james.메서드2()