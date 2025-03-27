tasks = ["Eat"]

# Lists all tasks, check if any exist, if so print it out nicely
def listTasks ():
    if len(tasks) == 0:
        print("\n" "No current tasks")
    else:
        print("------- Tasks -------")
        for i, value in enumerate(tasks, start=1):
            print(str(i) + ": " + value)
            

# Add a task, include input validation, checking for duplicates, empty strings, prompt for more tasks
def AddTask():
    adding = True
    added = False
    while(adding):
        addedTask = str(input("\nEnter in a task: "))
        duplicate = False
        for task in tasks:
            task = task[:-2]
            if (task.lower() == addedTask.lower()):
                duplicate = True
                break
        if(duplicate):
            print("Task already exists" + "\n")
        elif(len(addedTask) == 0 or len(addedTask.strip()) == 0):
            print("Nothing was entered try again")
        else:
            capitalizeFirst = addedTask[0].capitalize() + addedTask[1:]
            tasks.append(capitalizeFirst)
            listTasks()
            added = True
        while(added):
            cond = input("Add another task? Y = Yes, N = No: ")
            if cond == "Y" or cond =="y":
                break
            elif cond == "N" or cond == "n":
                adding = False
                added = False
            else:
                print("Incorrect Input")
                continue


# Remove a task
def removeTask():
    print("\n")
    try:
        taskNumber = int(input("Enter the number associated with the task you want to remove: "))
        if taskNumber < 0:
            print(f"{taskNumber} is negative and not a task.")
        else:
            print("Checking......")
    except ValueError:
        print("Not a valid number")
    try:
        tasks.pop(taskNumber - 1)
        print(f"Task removed" + "\n")
        listTasks()
    except IndexError:
        print("Task doesnt exist, try again")
    



# Mark as completed
def completeTask():
    listTasks()
    completedTask = int(input("\n" "Which task do you wish to complete?: "))
    try:
        if (tasks[completedTask - 1][-1] == "✅"):
            print(f"\nTask: '{tasks [completedTask - 1][:-2]}' has already been marked as completed")
        else:
            print("\nTask Completed\n")
            toUpdate = (tasks[completedTask - 1] + " ✅")
            tasks.pop(completedTask - 1)
            tasks.insert(completedTask - 1, toUpdate)
            listTasks()
    except IndexError:
        print(f"\nNo task labelled {completedTask}")

        




# Easy function to call the menu when needed
def displayMenu():
    print("------------------------------------------------- Task Manager Menu -------------------------------------------------")
    print("1: List Tasks")
    print("2: Add Tasks")
    print("3: Complete Tasks")
    print("4: Delete Task")
    print("5: Display Menu")
    print("6: Exit Manager")
    print("---------------------------------------------------------------------------------------------------------------------")




# Main program to keep things separated
def main():
    finished = False
    displayMenu()
    print("\n")

    while(not finished):
        try:
            function = int(input("Enter in the number for the request, e.g 5 = Display Menu: "))
            if(function == 1):
                listTasks()
                print("\n")
            elif(function == 2):
                AddTask()
                print("\n")
            elif(function == 3):
                completeTask()
                print("\n")
            elif(function == 4):
                removeTask()
                print("\n")
            elif(function == 5):
                displayMenu()
                print("\n")
            elif(function == 6):
                print("Closing down manager")
                quit()
            else:
                print(f"Number {function} has no method, input must be between 1-6." + "\n")
        except ValueError:
            print("That's not a number, input must be between 1-6" + "\n")
        
            
main()
