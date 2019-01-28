# define the task array to be manipulated
taskArray = []

# define main function to call overall task function
def main():
    # task()
    addToFile()

# # define file to import and update the list
def addToFile():
    f = open("taskFile.txt", "w")
    f.write("hello world")
    # f = open('taskFile', 'r')
    # f.readlines()

# define task function to prompt for and execute action functions
def task():

    print(f"Congratulation you are running Autumn's Task List Program\nWhat would you like to do next?\n1. List all tasks\n2. Add a task to the list.\n3. Delete a task.\n0. To quit the program\n")

    choice = input("Please choose an option above: ")
    while choice != "0":

        if choice == "1":
            listAll()

        elif choice == "2":
            addTask()

        elif choice == "3":
            deleteTask()

        elif choice != "1" and choice != "2" and choice != "3" and choice != "0":
            print("invalid entry")

        choice = input("What would you like to do next?\n1. List all tasks\n2. Add a task to the list.\n3. Delete a task.\n0. To quit the program\n")

# action function - list all items in the list
def listAll():
    for items in taskArray:
        print(items)

# action function - add items to the list
def addTask():
    addThis = input("What task would you like to add?\n").lower()
    while addThis != "q":
        taskArray.append(addThis)
        addThis = input("Enter another task or enter q\n").lower()
        listAll()

# action function - delete items from the list
def deleteTask():
    listAll()
    deleteThis = input("What task would you like to delete?\n").lower()
    while deleteThis != "q":
        if deleteThis in taskArray:
            taskArray.remove(deleteThis)
            deleteThis = input("Enter another task to delete or enter q\n").lower()
            listAll()
        else:
            print("invalid entry")
            break

if __name__ == '__main__':
    main()