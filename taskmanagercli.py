import json
from datetime import datetime
import os

#Add a task function
def task_add():
    # Load Tasks
    with open("tasks.json", "r") as f:
        tasks = json.load(f)

    # id: A unique identifier for the task
    task_id = len(tasks) + 1
    
    # description: A short description of the task
    task_desc = input("Add description: ")
    
    # status: The status of the task (todo, in-progress, done)
    task_status = "in-progress"
    
    # createdAt: The date and time when the task was created
    task_createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #updatedAt: The date and time when the task was last updated
    task_updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # JSON dict
    task_data = {
        "task_id": task_id,
        "task_desc": task_desc,
        "task_status": task_status,
        "task_createdAt": task_createdAt,
        "task_updatedAt": task_updatedAt
    }          
        
    tasks.append(task_data)
    
    with open(r"tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
        
    print(f"Task added successfully (ID: {task_id})")


#Update function
def task_update():
    # Load Tasks
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    
    update_id = int(input("Enter task ID to update: "))

    # Find the task by ID
    update_id_data = next((task for task in tasks if task["task_id"] == update_id), None)

    if update_id_data:
        new_desc = input("Enter new description: ")
        update_id_data["task_desc"] = new_desc

        # Updates task_updatedAt
        update_id_data["task_updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Saves task desc + updatedAt to JSON file
    with open("tasks.json", "w") as f:
        json.dump(tasks,  f,  indent=4)


#Delete function
def task_delete():
    # Load Tasks
    with open("tasks.json", "r") as f:
        tasks = json.load(f)

        delete_id = int(input("Enter task ID to delete: "))
        new_tasks = [task for task in tasks if task["task_id"] != delete_id]

        with open("tasks.json", "w") as f:
            json.dump(new_tasks, f, indent=4)

task_update()