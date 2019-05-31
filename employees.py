# Multiple inhertiance demo with employees
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"


class Programmer(Employee):
    def __init__(self, id, name, lang, salary):
        print(type(self))
        Employee.__init__(self, id, name)
        self.lang = lang
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"{self.id} - {self.name} - {self.lang} - {self.salary}"


class Dba(Employee):
    def __init__(self, id, name, database, hours, rate):
        Employee.__init__(self, id, name)
        self.database = database
        self.hours = hours
        self.rate = rate

    def get_salary(self):
        return self.hours * self.rate

    def __str__(self):
        return f"{self.id} - {self.name} - {self.database} - {self.hours * self.rate}"


class ProgrammerDba(Programmer, Dba):
    def __init__(self, id, name, lang, database, salary, hours, rate):
        Programmer.__init__(self, id, name, lang, salary)
        Dba.__init__(self, id, name, database, hours, rate)

    def get_salary(self):
        return Programmer.get_salary(self) + Dba.get_salary(self)


p = Programmer(1, "Abc", "Python", 60000)
print(p)
d = Dba(2, "Pqr", "Oracle", 10, 1000)
print(d)
b = ProgrammerDba(3, "Xyz", "Python", "Oracle", 40000, 20, 500)
print(b)
print(b.get_salary())
