# Multiple inheritance demo 

from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, admno, name):
        self.admno = admno
        self.name = name

    @abstractmethod
    def get_marks(self):
        pass


class JavaStudent(Student):
    def __init__(self, admno, name, theory_marks):
        Student.__init__(self,admno, name)
        self.theory_marks = theory_marks

    def get_marks(self):
        return self.theory_marks


class PythonStudent(Student):
    def __init__(self, admno, name, lab_marks):
        Student.__init__(self, admno, name)
        self.lab_marks = lab_marks

    def get_marks(self):
        return self.lab_marks


class JythonStudent(JavaStudent, PythonStudent):
    def __init__(self, admno, name, theory_marks, lab_marks):
        JavaStudent.__init__(self, admno, name, theory_marks)
        PythonStudent.__init__(self, admno, name, lab_marks)

    def get_marks(self):
        return JavaStudent.get_marks(self) + PythonStudent.get_marks(self)


js = JavaStudent(101, "James", 80)
ps = PythonStudent(102, "Van", 87)
jys = JythonStudent(103, "James Van", 76, 80)
print(js.get_marks(), ps.get_marks(), jys.get_marks())
