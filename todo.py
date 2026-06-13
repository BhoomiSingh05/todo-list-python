tasks = []
history = []

while True:
    print("\n--- TO-DO LIST APP ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. View History")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_tasks = input("Enter task(s) separated by commas: ")

        for task in new_tasks.split(","):
            task = task.strip()
            if task:
                tasks.append(task)
                history.append(f"Added: {task}")

        print("Task(s) added successfully.")

    elif choice == "3":
        if not tasks:
            print("No tasks available to delete.")
        else:
            try:
                task_num = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_num - 1)

                history.append(f"Deleted: {removed}")

                print(f"'{removed}' has been removed successfully.")

            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")

    elif choice == "4":
        if not history:
            print("No history available.")
        else:
            print("\n--- TASK HISTORY ---")
            for item in history:
                print(item)

    elif choice == "5":
        print("Goodbye! Thanks for tracking your goals.")
        break

    else:
        print("Invalid option selected. Please pick a number from 1 to 5.")
