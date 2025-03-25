import json
from datetime import datetime
import os
import colourOutput as co

#Add a task function
def task_add():
    # Load Tasks
    tasks = load_tasks()

    # id: A unique identifier for the task
    task_id = len(tasks) + 1
    
    # description: A short description of the task
    task_desc = input("\nAdd description: ")
    
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
        
    print(f"\nTask added successfully (ID: {task_id})\n")
    print("\n" + "-" * 30 + "\n")

#Update desc
def task_update_desc():
    # Load Tasks
    tasks = load_tasks()
    if not tasks:
        print("No tasks available")
        return
    
    print("-" * 30 + "\n")
    print("\nAvailable Tasks:\n")
    for task in tasks:
        status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
        print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
        print("-" * 30 + "\n")
    
    update_id = int(input("\nEnter task ID to update: "))

    # Find the task by ID
    update_id_data = next((task for task in tasks if task['task_id'] == update_id), None)

    if update_id_data:
        new_desc = input("\nEnter new description: ")
        update_id_data["task_desc"] = new_desc

        # Updates task_updatedAt
        update_id_data["task_updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        print(f"\nDescription for ID: {update_id_data['task_id']} has been changed to:\n{new_desc}")
        print("\n" + "-" * 30 + "\n")


    # Saves task desc + updatedAt to JSON file
    with open("tasks.json", "w") as f:
        json.dump(tasks,  f,  indent=4)


#Delete function
def task_delete():
    try:
        # Load Tasks
        tasks = load_tasks()
        if not tasks:
            print("No tasks to display")
            return

        print("-" * 30 + "\n")
        print("\nAvailable Tasks:\n")
        for task in tasks:
            status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
            print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
            print("-" * 30 + "\n")
        
        # User input
        while True:
            try:
                task_delete_id = int(input("\nEnter task ID to delete (Press 0 to opt out): "))
            except ValueError:
                print("\nProvided number is not valid \nPlease try again...")
                
            if task_delete_id == 0:
                break
            else:
                if task_delete_id:
                    #Filtering tasks
                    new_tasks = [task for task in tasks if task["task_id"] != task_delete_id]
                    with open("tasks.json", "w") as f:
                        json.dump(new_tasks, f, indent=4)
                    
                    print(f"\nSuccessfully deleted task {task_delete_id}")
                    break
    
    except FileNotFoundError:
        print("No tasks file found!")
    except json.JSONDecodeError:
        print("Invalid JSON format in tasks file!")
    except Exception as e:
        print(f"An error occured: {e}")

def task_list():
    try:
    # Load Tasks
        tasks = load_tasks()
        if not tasks:
            print("No tasks available")
            return

        while True:
            print("-" * 30 + "\n")
            print("Select filter:")
            print("View all tasks: 1")
            print("View tasks in-progress: 2")
            print("View tasks done: 3")
            print("Opt out: 4")
            
            task_list_choice = int(input("\nEnter value for list: "))

            if task_list_choice == 1:
                print("-" * 30 + "\n")
                print("\nList of all tasks:\n")
                for task in tasks:
                    status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
                    print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
                    print("-" * 30 + "\n")
            elif task_list_choice == 2:
                in_progress_tasks = [task for task in tasks if task['task_status'] == 'in-progress']
                print("-" * 30 + "\n")
                print("\nList of in-progress tasks:\n")
                for task in in_progress_tasks:
                    status_color = co.ORANGE
                    print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
                    print("-" * 30 + "\n")
            elif task_list_choice == 3:
                done_tasks = [task for task in tasks if task['task_status'] == 'done']
                print("-" * 30 + "\n")
                print("\nList of done tasks:\n")
                for task in done_tasks:
                    status_color = co.GREEN
                    print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
                    print("-" * 30 + "\n")
            if task_list_choice == 4:
                print("Opting out")
                break
            else:
                print("Invalid number")

    except FileNotFoundError:
        print("No tasks file found!")
    except json.JSONDecodeError:
        print("Invalid JSON format in tasks file!")
    except Exception as e:
        print(f"An error occured: {e}")

def task_update_status():
    try:
    # Load Tasks
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        
        print("-" * 30 + "\n")
        print("\nAvailable Tasks:\n")
        print("\n" + "-" * 30 + "\n")
        for task in tasks:
            status_color = co.ORANGE if task['task_status'] == "in-progress" else co.GREEN
            print(f"ID: {task['task_id']} | Task: {task['task_desc']} | Status: {status_color}{task['task_status']}{co.RESET} | Date created: {task['task_createdAt']} | Date Updated: {task['task_updatedAt']}")
            print("\n" + "-" * 30 + "\n")

        while True:
            try:
                task_id_update = int(input("\nEnter task ID to update: "))
                task_to_update = next((task for task in tasks if task['task_id'] == task_id_update), None)
                if task_to_update is None:
                    print("\nTask not found!")
                    continue
                
                # Instead of having user writing either in-progress or done
                # The codes updates it itself. Nice
                if task_to_update['task_status'] == 'in-progress':
                    task_to_update['task_status'] = 'done'
                else:
                    task_to_update['task_status'] = 'in-progress'

                with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=4)

                print(f"\nStatus for ID {task_id_update} has been updated to {task_to_update['task_status']}")
                break

            except ValueError as e:
                print(f"\nInvalid input: {e}\n")

    except FileNotFoundError:
        print("No tasks file found!")
    except json.JSONDecodeError:
        print("Invalid JSON format in tasks file!")
    except Exception as e:
        print(f"An error occured: {e}")

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No tasks file found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON formart in tasks file")
        return []