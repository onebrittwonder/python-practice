# to do list

task_list = []

def complete_task():
    task_index = int(input("\nEnter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(task_list):
        task_list[task_index]["done"] = True
        print("\nTask marked as done!")
    else:
        print("\nInvalid task number")

def check_tasks():
    if task_list:
        print("\nTasks:")
        for index, task in enumerate(task_list):
            status = "done" if task["done"] else "not done"
            print(f"{index + 1}. {task['task']} - {status}")
    else:
        print("\nTask list is empty")

def add_task():
    n_tasks = int(input("\nHow many tasks to add:  "))

    for i in range(n_tasks):
        task = input("\nPlease enter a task: ")
        task_list.append({"task": task, "done": False})
        print("\nTask added!")

def main():
    print("\nWelcome to your To-Do List! What would you like to do?")

    while True:
        action = input("""   
            1. Add Task 
            2. Complete Task
            3. Check Tasks
            4. Exit To-Do List
                    
            Type number corresponding to choice above: """)
        
        if action == "1":
            add_task()
        elif action == "2":
            complete_task()
        elif action == "3":
            check_tasks()
        elif action == "4":
            print("\nExiting To-Do List...")
            break
        else:
            print("\nInvalid choice. Try again")

if __name__ == "__main__":
    main()