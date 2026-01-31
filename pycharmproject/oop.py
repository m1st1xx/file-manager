class student:
    def __init__(self,name,family,age,marks):
        self.name=name
        self.family=family
        self.age=age
        self.marks=marks
    def say_info(self):
        return f"name: {self.name},family: {self.family},age: {self.age},marks: {self.marks} "
    def add_mark(self,newmark):
        (self.marks).append(newmark)
        return f"mark added: {self.marks}"
    def srarm(self):
        return sum(self.marks)/len(self.marks)
mystud=student("олег","собакен",26,[5,4,4,3])
print(mystud.say_info())
print(mystud.add_mark(int(input())))
print(mystud.srarm())