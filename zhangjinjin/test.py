class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ",Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Zara", 2000)
emp1.displayCount()
emp2.displayCount()
emp1.displayEmployee()
emp2.displayEmployee()

print(Employee.__module__)

