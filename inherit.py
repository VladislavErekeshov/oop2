class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        print("Создан SchoolMember: {0}".format(self.name))

    def tell(self):
        print('Имя: "{0}", возраст: "{1}"'.format(self.name, self.age), end = " ")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

        print('создан Teacher: "{0}"'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

        print('Создан Student: "{0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки :"{0:d}"'.format(self.marks))

t = Teacher("Kiruha", 9, 100000)
s = Student("Oleg", 1, 1488)

print()

members = [t, s]

for member in members:
    member.tell()