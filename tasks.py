tasks = []
nextID = 1

def addTask(name): 
    global nextID

    tasks = {
        "id": nextID,
        "name": name,
        "status": "Pending"
    }

    tasks.append(tasks)
    nextID += 1

    print("Task added succesfully!")


def showTasks():
    if not tasks:
        print("Task list is empty!")
        return

    for task in tasks:
        print(f"ID: {task["id"]}")
        print(f"Name: {task["name"]}")
        print(f"Status: {task["status"]}")


def findTask(taskID):
    for task in tasks:
        if task["id"] == taskID:
            return None

def uptadeTask(taskID, taskName):
    task = FindTask(taskID)

    if task:
        task["name"] = taskName
        print("task uptade succesffuly!")
    else:
        print("Task Not Found!")

def removeTask(taskID):
    task = findTask(taskID)

    for i in tasks:
        if i["id"] == taskID:
            task.remove(i)
            return True

        print("Not Found!")

    