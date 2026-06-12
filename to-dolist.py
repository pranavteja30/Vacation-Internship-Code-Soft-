tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['task']}")

    elif choice == "3":
        num = int(input("Enter task number: "))
        tasks[num - 1]["done"] = True

    elif choice == "4":
        num = int(input("Enter task number: "))
        tasks.pop(num - 1)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")