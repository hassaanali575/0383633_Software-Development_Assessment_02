from datetime import datetime

TASK_FILE = "tasks.txt"
tasks = []


# function to load task files saved
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            loaded_tasks = eval(file.read())
            return loaded_tasks if isinstance(loaded_tasks, list) else []
    except FileNotFoundError:
        return []


# Function for saving task in the file
def save_tasks():
    with open(TASK_FILE, 'w') as file:
        file.write(str(tasks))


# Function to display the task  saved in the file
def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            due_date = task.get('due_date', 'N/A')
            priority = task.get('priority', 'N/A')
            category = task.get('category', 'N/A')
            print(f"{idx}. {task['name']} - {status} | Due: {due_date} | Priority: {priority} | Category: {category}")


# Function to add task with name user input
def add_task(name):
    new_task = {
        'name': name,
        'created_at': str(datetime.now()),
        'completed': False
    }
    tasks.append(new_task)
    save_tasks()
    print(f"Task '{name}' added successfully.")


# Function to mark any task from list as complete
def mark_completed(name):
    matching_tasks = [task for task in tasks if task['name'] == name]
    if matching_tasks:
        for task in matching_tasks:
            task['completed'] = True
        save_tasks()
        print(f"Task '{name}' marked as completed.")
    else:
        print("Task not found.")


# Function to delete any task created or added in task Management System
def delete_task(name):
    matching_tasks = [task for task in tasks if task['name'] == name]
    if matching_tasks:
        for task in matching_tasks:
            tasks.remove(task)
        save_tasks()
        print(f"Task '{name}' deleted successfully.")
    else:
        print("Task not found.")


# Function for defining the Priority of any task over other task
def prioritize_task(name, priority):
    matching_tasks = [task for task in tasks if task['name'] == name]
    if matching_tasks:
        for task in matching_tasks:
            task['priority'] = priority
        save_tasks()
        print(f"Priority set for task '{name}'.")
    else:
        print("Task not found.")


# Function to for deadline to set the date for task
def set_due_date(name, due_date):
    matching_tasks = [task for task in tasks if task['name'] == name]
    if matching_tasks:
        for task in matching_tasks:
            task['due_date'] = due_date
        save_tasks()
        print(f"Due date set for task '{name}'.")
    else:
        print("Task not found.")


# Function to categorize the task in created defined by user
def categorize_task(name, category):
    matching_tasks = [task for task in tasks if task['name'] == name]
    if matching_tasks:
        for task in matching_tasks:
            task['category'] = category
        save_tasks()
        print(f"Category set for task '{name}'.")
    else:
        print("Task not found.")


# Function to search the task in available added task list
def search_tasks(keyword):
    matching_tasks = [task for task in tasks if keyword.lower() in task['name'].lower()]
    if matching_tasks:
        print("Matching Tasks:")
        for idx, task in enumerate(matching_tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            due_date = task.get('due_date', 'N/A')
            priority = task.get('priority', 'N/A')
            category = task.get('category', 'N/A')
            print(f"{idx}. {task['name']} - {status} | Due: {due_date} | Priority: {priority} | Category: {category}")
    else:
        print("No matching tasks found.")


# Main Function to Load task and display Menu Option to users
def main():
    global tasks
    tasks = load_tasks()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Prioritize Task")
        print("6. Set Due Date")
        print("7. Categorize Task")
        print("8. Search Tasks")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            task_name = input("Enter the task name to mark as completed: ")
            mark_completed(task_name)
        elif choice == '4':
            show_tasks()
            task_name = input("Enter the task name to delete: ")
            delete_task(task_name)
        elif choice == '5':
            show_tasks()
            task_name = input("Enter the task name to prioritize: ")
            priority = input("Enter priority (High, Medium, Low): ")
            prioritize_task(task_name, priority)
        elif choice == '6':
            show_tasks()
            task_name = input("Enter the task name to set due date: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            set_due_date(task_name, due_date)
        elif choice == '7':
            show_tasks()
            task_name = input("Enter the task name to categorize: ")
            category = input("Enter category: ")
            categorize_task(task_name, category)
        elif choice == '8':
            keyword = input("Enter keyword to search for tasks: ")
            search_tasks(keyword)
        elif choice == '9':
            print("Exiting Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
