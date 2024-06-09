# Global variables
tasks = []

# Helper functions
def PrintList():
    print("\nCURRENT LIST:")
    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

# Program code
def main():
    
    # Program runs until the user decides to exit
    while True: 
        print("\n===== TO DO LIST =====")
        print("1. Add Tasks")
        print("2. Show Tasks")
        print("3. Complete Tasks")
        print("4. Exit Program")

        choice = input("Enter Choice: ")
        
        if choice == "1":
            print()
            n_tasks = int(input("Enter quantity of tasks to add: "))

            for i in range(n_tasks):
                task = input(f"Enter Task: ")
                tasks.append({"task": task, "completed": False})
                print(f"Added Task: {task}")
                # Testing Only
                print(tasks)                     

        
        elif choice == "2":
            PrintList()

        elif choice == "3":
            return               

        elif choice == "4":
            return

main()
