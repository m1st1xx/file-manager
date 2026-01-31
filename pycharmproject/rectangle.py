class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def square(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length + self.width) * 2
    def say_info(self):
        return f"length: {self.length} width: {self.width}"
my_rectangle=rectangle(int(input("input length: ")),int(input("input width: ")))
print(my_rectangle.square())
print(my_rectangle.perimeter())
print(my_rectangle.say_info())
