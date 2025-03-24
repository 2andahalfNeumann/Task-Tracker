import json
from datetime import datetime
import os
import colourOutput as co

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
    """
    Added error handling
    """
    
    try:
        # Load Tasks
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

        print("-" * 30 + "\n")
        print("\nAvailable Tasks:\n")
        for task in tasks:
            status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
            print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
            print("-" * 30 + "\n")
        
        # User input
        while True:
            try:
                delete_id = int(input("\nEnter task ID to delete: "))
                break
            except ValueError:
                print("Provided number is not valid \nPlease try again...")

        #Filtering tasks
        new_tasks = [task for task in tasks if task["task_id"] != delete_id]

        with open("tasks.json", "w") as f:
            json.dump(new_tasks, f, indent=4)
        
        print(f"Successfully deleted task  {task['task_id']}")
    
        """
        Currently added "errno" I stumbled across whilst testing.
        """
    except FileNotFoundError:
        print("No tasks file found!")
    except json.JSONDecodeError:
        print("Invalid JSON format in tasks file!")
    except Exception as e:
        print(f"An error occured: {e}")

def task_list():
    try:
    # Load Tasks
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

        print("-" * 30 + "\n")
        print("\nAvailable Tasks:\n")
        for task in tasks:
            status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
            print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
            print("-" * 30 + "\n")

    except FileNotFoundError:
        print("No tasks file found!")
    except json.JSONDecodeError:
        print("Invalid JSON format in tasks file!")
    except Exception as e:
        print(f"An error occured: {e}")

def task_update():
    try:
    # Load Tasks
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        
        print("-" * 30 + "\n")
        print("\nAvailable Tasks:\n")
        for task in tasks:
            status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
            print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
            print("-" * 30 + "\n")

        while True:
            try:
                task_id_update = int(input("\nEnter task ID to update: "))
                task_to_update = next((task for task in tasks if task['task_id'] == task_id_update), None)

                if task_to_update is None:
                    print("Task not found!")
                    continue

                while True:
                    new_status = input("Enter new status ('in-progress' or 'done'): ")
                    if new_status in ['in-progress', 'done']:
                        break
                    print("Invalid status! Please enter 'in-progress' or 'done'")

                # Update task status
                task_to_update['task_status'] = new_status

                with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=4)

                print(f"\nTask {task_id_update} has been updated")
                break

            except ValueError as e:
                print(f"Invalid input: {e}\n")

    except FileNotFoundError:
        print("No tasks file found!")
    except json.JSONDecodeError:
        print("Invalid JSON format in tasks file!")
    except Exception as e:
        print(f"An error occured: {e}")