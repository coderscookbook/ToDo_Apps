'''
####################################################################################
TODO:
# 1. Add error handling for invalid inputs
# 2. Add ability to add new lists
# 3. Save lists to file
# 4. Change console text color for improved user experience
####################################################################################
'''

# Import modules
import os

# Global variables
tasks = []

####################################################################################
# Helper Functions                                                                 #
####################################################################################
def ClearConsole():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux (os.name = 'posix')
    else:
        os.system('clear')

def PrintMenu():
    print("\n===== MENU =====")
    print("1. Add Tasks")
    print("2. Show Tasks")
    print("3. Complete Tasks")
    print("4. Exit Program")

def PrintList():
    print("\n===== CURRENT LIST =====")
    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")


####################################################################################
# Program Code                                                                     #
####################################################################################
def main():
    
    # Program runs until the user decides to exit
    while True: 
        PrintMenu()
        choice = input("Enter Choice: ")
       
        # Menu cases
        if choice == "1":
            ClearConsole()
            n_tasks = int(input("Enter quantity of tasks to add: "))

            for i in range(n_tasks):
                task = input(f"Enter Task: ")
                tasks.append({"task": task, "completed": False})
                print(f"Task Added!")
                # Testing Only
                # print(tasks)                     

        elif choice == "2":
            ClearConsole()
            PrintList()

        elif choice == "3":
            ClearConsole()
            PrintList()
            task_index = int(input("Enter Task # to Mark as Completed: "))
            if 0 <= task_index < len(tasks) + 1:
                tasks[task_index-1]["completed"] = True
                print(f"{tasks[task_index-1]['task']} marked completed!")
            else:
                print("Invalid task number. Try again.")

        elif choice == "4":
            print("EXITING TO-DO LIST.")
            break

        # If user enters invalid menu option
        else:
            print("Invalid Choice. Try again.")
if __name__ == "__main__":
    main()
