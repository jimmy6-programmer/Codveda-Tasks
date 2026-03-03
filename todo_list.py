import json
import os

FILE_NAME = 'tasks.json'

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
else:
    tasks = []

def save_task():
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

while True:
    print("\n --- This is our to-do list app ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit App")

    choice = input("Enter option 1-5: ")

    if choice == "1":
        title = input("Enter task title: ")
        task = {
            'title': title,
            'completed': False
        }
        tasks.append(task)
        save_task()
        print("Task added successfully")
    elif choice == "2":
        if not tasks:
            print("No available tasks at the moment")
        else:
            print("\n Your tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{index}. {task['title']} [{status}]")
    elif choice == "3":
        if not tasks:
            print("No available task to delete")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{index}. {task['title']} [{status}]")
            try:
                task_num = int(input("Enter task number, to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_task()
                    print(f"Task {deleted_task['title']} was deleted successfully")
            except ValueError:
                print("Invalid number option")
    elif choice == "4":
        if not tasks:
            print("No available task to mark as done")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "Done" if task['completed'] else "Not done"
                print(f"{index}. {task['title']} [{status}]")
            try:
                task_num = int(input("Enter task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    save_task()
                    print(f"Task '{tasks[task_num- 1]['title']}' was marked as done")
                else:
                    print("Invalid option")
            except json.JSONDecodeError:
                print("Invalid number option")
    elif choice == "5":
        print("Goodbye!, see you next time")
        break
    else:
        print("You have entered an invalid choice, try again")                                                     

