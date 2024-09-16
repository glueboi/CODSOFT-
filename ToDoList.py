import os

class Task:
    def __init__(self, task):
        self.task = task
        self.status = 'Pending'

    def done(self):
        self.status = 'Completed'

    def __str__(self):
        return f"{self.task} - {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.loadfromfile()  # Automatically load tasks on start

    def addtask(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)
        print(f"\nTask '{task_name}' added.")

    def showtasks(self):
        if len(self.tasks) == 0:
            print("\nNo tasks to show.")
        else:
            print("\n--- To-Do List ---")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def completetask(self, task_index):
        try:
            task = self.tasks[task_index]
            task.done()
            print(f"\nTask '{task.task}' marked as completed.")
        except IndexError:
            print("\nInvalid task number!")

    def deletetask(self, task_index):
        try:
            deleted_task = self.tasks.pop(task_index)
            print(f"\nTask '{deleted_task.task}' deleted.")
        except IndexError:
            print("\nInvalid task number!")

    def savetofile(self):
        with open('todo_list_data.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task.task},{task.status}\n")
        print("\nTasks saved to file.")

    def loadfromfile(self):
        if os.path.exists('todo_list_data.txt'):
            with open('todo_list_data.txt', 'r') as file:
                for line in file.readlines():
                    task_name, status = line.strip().split(',')
                    task = Task(task_name)
                    task.status = status
                    self.tasks.append(task)
            print("\nLoaded tasks from file.")
        else:
            print("\nNo previous tasks found.")

def runapp():
    todo = ToDoList()

    while True:
        print("\n--- Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task_name = input("What's the task? ")
            todo.addtask(task_name)
        elif choice == '2':
            todo.showtasks()
        elif choice == '3':
            todo.showtasks()
            try:
                task_num = int(input("Which task to complete (number)? ")) - 1
                todo.completetask(task_num)
            except ValueError:
                print("\nEnter a valid number.")
        elif choice == '4':
            todo.showtasks()
            try:
                task_num = int(input("Which task to delete (number)? ")) - 1
                todo.deletetask(task_num)
            except ValueError:
                print("\nEnter a valid number.")
        elif choice == '5':
            todo.savetofile()
            print("\nGoodbye!")
            break
        else:
            print("\nNot a valid choice, try again.")

if __name__ == "__main__":
    runapp()
