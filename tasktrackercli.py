import os
import json
from datetime import datetime

def task_add():
    
    # id: A unique identifier for the task
    task_id = input("Add Task: ")
    
    # description: A short description of the task
    task_desc = input("Add description: ")
    
    # status: The status of the task (todo, in-progress, done)
    task_status = input("Add Status: ")
    
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
    
    
    # Json
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    
    tasks.append(task_data)

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    
    """
    print("\nTask details are as follows:")
    print("ID:", task_id)
    print("Description:", task_desc)
    print("Status:", task_status)
    print("Created At:", task_createdAt)
    print("Updated At:", task_updatedAt)
    """
    
task_add()