def main():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            new_task = input("Enter task: ").strip()
            if new_task:
                tasks.append(new_task)
                print("Task added successfully!")
            else:
                print("Error: Task cannot be empty.")
                
        elif choice == "2":
            print("\n--- Current Tasks ---")
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            print("---------------------")
            
        elif choice == "3":
            print("Exiting app. Goodbye!")
            break
            
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()