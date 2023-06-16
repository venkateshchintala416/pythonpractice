class CheckSalary(Exception):

    def empSalary(self, salary):
        if salary > 50000:
            raise CheckSalary('Salary is out of range')
        else:
            print('Salary is ', salary)

c = CheckSalary()
c.empSalary(45000)
