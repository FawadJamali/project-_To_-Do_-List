import os

# Function to display the menu
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a task
def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

# Function to mark a task as done
def mark_done(tasks, index):
    if index >= 1 and index <= len(tasks):
        tasks[index - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(tasks, index):
    if index >= 1 and index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter the task index to mark as done: "))
            mark_done(tasks, index)
        elif choice == "4":
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
