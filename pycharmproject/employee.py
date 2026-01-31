class employee:
    def __init__(self,name ,title,salary):
        self.name=name
        self.title=title
        self.salary=salary
        self.employees=[]
    def get_info(self):
        return f"name employee: {self.name}, title: {self.title}, salary: {self.salary}"
    def promotion(self,new_title):
        self.title=new_title
        return f"promotion changed, now employee is: {self.title}"
    def new_salary(self,percent):
        self.salary=self.salary+(self.salary*(percent/100))
        return f"salary changed, new salary of employee: {self.salary}"
    def compare(self,other_employee):
        if self.salary> other_employee.salary:
            return f"salary of {self.name} is bigger than {other_employee.name} "
        else:
            return f"salary of {other_employee.name} is bigger than {self.name} "

employee1=employee("vanya","manager",50000)
employee2=employee("igor","junior",40000)

print(employee1.get_info())
print(employee1.promotion("great manager"))
print(employee1.new_salary(50))
print(employee1.get_info())
print(employee1.compare(employee2))
