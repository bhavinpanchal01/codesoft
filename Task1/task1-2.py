import sys
from task1 import ToDoList

def show_menu():
    """Display the menu options to the user."""
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.view_tasks()

        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_id = int(input("Enter task number to update: "))
                print("1. Update Task")
                print("2. Mark as Completed")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    new_task = input("Enter the new task description: ")
                    todo_list.update_task(task_id, new_task=new_task)
                elif sub_choice == "2":
                    todo_list.update_task(task_id, mark_done=True)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_id = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
