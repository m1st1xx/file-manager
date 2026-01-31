class Task:
    def __init__(self,name,description,status,priority,deadline):
        self.name=name
        self.description=description
        self.status=status
        self.priority=priority
        self.deadline=deadline

    def __repr__(self):
        return f"{self.name},{self.status},{self.priority}"
class Taskmanager:
    def __init__(self):
        self.tasks=[]
    def add_task(self,name,description,status,priority,deadline):
        new_task=Task(name,description,status,priority,deadline)
        self.tasks.append(new_task)
        return f"task - {name} added"
    def get_info(self):
        return self.tasks
    def change_status(self,title,new_status):
        for task in self.tasks:
            if task.name==title:
                task.status=new_status
                return f"status {title} changed"
    def remove_task(self,title):
        for task in self.tasks:
            if task.name==title:
                self.tasks.remove(task)
                return f"task {title} removed"


taski=Taskmanager()
print(taski.add_task("посрать","посрать","не начата","высокий приоритет","now"))
print(taski.add_task("поссать","поссать","в процессе","высокий приоритет","now"))
print(taski.add_task("сделать уроки","алгебра геометрия","не начата","низкий приоритет","now"))
print(taski.get_info())
print(taski.remove_task("поссать"))
print(taski.change_status("сделать уроки","завершена"))
print(taski.get_info())
