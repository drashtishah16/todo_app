todo_items = []

def show_menu():
    print("\n===== TODO MENU =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task_name = input("Enter the task: ").strip()
    if task_name:
        todo_items.append(task_name)
        print("Task added.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if len(todo_items) == 0:
        print("No tasks found.")
    else:
        print("\nYour Todo List:")
        for index, task in enumerate(todo_items, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if todo_items:
        try:
            number = int(input("Enter task number to remove: "))
            deleted = todo_items.pop(number - 1)
            print(f"Removed task: {deleted}")
        except (ValueError, IndexError):
            print("Please enter a valid task number.")

while True:
    show_menu()
    user_choice = input("Select an option (1-4): ")

    if user_choice == "1":
        add_task()
    elif user_choice == "2":
        view_tasks()
    elif user_choice == "3":
        remove_task()
    elif user_choice == "4":
        print("Thank you , exiting...!")
        break
    else:
        print("Invalid choice. Try again.")