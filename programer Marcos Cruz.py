class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work" % self.name)


person = Person("name", "education")


class Employee(Person):
    def __init__(self, job, name):
        super(Employee, self).__init__(job, name)
        self.job = job
        self.name = name

    def job(self):
        print("%s goes to his job" % self.name)


employee = Employee("job", "name")


class Programmer(Employee):
    def __init__(self, job, name, computer):
        super(Programmer, self).__init__(job, name)
        self.computer = computer

    def code(self):
        print("%s is coding on a %s" % (self.name, self.computer))


programmer = Programmer("computer", "job", "name")
