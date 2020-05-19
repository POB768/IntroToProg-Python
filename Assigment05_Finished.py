# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PO'Brien,5.18.2020,Added the ToDo code sections to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
todoFile = open(objFile, 'w')  # had to add this to make it run in command prompt, wouldn't run even with pre-created
# txt file

strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
todoFile = open(objFile, 'r')
for row in todoFile:
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1]}
    lstTable.append(dicRow)
todoFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for dicRow in lstTable:
            print(dicRow['Task'] + ',' + dicRow['Priority'])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        taskInput = input("Enter tasK: ")
        priorityInput = input("Enter priority: ")
        dicRow = {'Task': taskInput.lower(), 'Priority': priorityInput}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        delTask = input('Enter task to be deleted: ')

        for dicRow in lstTable:
            if delTask.lower() == dicRow['Task']:
                lstTable.remove(dicRow)
                print('Task Deleted!')
            else:
                print('This task is not in your list')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        todoFile = open(objFile, 'w')
        for dicRow in lstTable:
            todoFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')

        print('Tasks with priorities saved to file!')
        todoFile.close()
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print('Goodbye')
        break  # and Exit the program
