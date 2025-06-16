tasks = [
    "Write unit tests for API endpoints",
    "Analyze customer reviews for sentiment",
    "Create data visualization with matplotlib",
    "Optimize database queries for performance",
    "Add pagination to product listings",
    "Improve error handling mechanisms",
    "Refactor code for better readability",
    "Add logging to track application flow",
    "Design and implement a cache layer",
    "Write comprehensive API documentation"
]
# Display Tasks
def displayList():
    for x in range (len(tasks)):
        print(f"{x+1}) {tasks[x]}")

# Add NEW Tasks
def addTask():
    print("Please Enter Task")
    newTask = str(input())
    tasks.append(newTask)
    print("Updated List")
    displayList()
    
# Remove Tasks
def removeTask():
    displayList()
    print("Select index of Task You want to Delete")
    removeNum= int(input())
    tasks.pop(removeNum-1)
    print("Updated List")
    displayList()
options ="""Please Select
1) Display Tasks
2) Add Task
3) Delete Task"""
print(options)
userChoice = int(input())
if userChoice == 1:
    displayList()
elif userChoice==2:
    addTask()
elif userChoice==3:
    removeTask()