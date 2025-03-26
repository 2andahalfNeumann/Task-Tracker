# Task Manager CLI

A simple command-line task management application written in Python. This tool allows you to add tasks, update descriptions, change task status, delete tasks, and view a list of tasks with simple color-coded status output.

All code was intended to follow:
[The Roadmap.sh's task-tracker Project](https://roadmap.sh/projects/task-tracker)

However, I sligtly differed as to making a cmd promt menu instead of pure cli.

---

## Table of Contents

- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

---

## Features

- **Add Task:** Create a new task with a description, initial status, and timestamps.
- **Edit Task Description:** Update the description of an existing task.
- **Update Task Status:** Toggle task status between _in-progress_ and _done_.
- **Delete Task:** Remove a task from the task list.
- **Task List:** View all tasks, tasks in-progress, or tasks that are done with color-coded output.

---

## File Structure

- **main.py:**  
  Entry point for the CLI application. Displays options and routes user inputs to the appropriate task management functions.

- **taskmanagercli.py:**  
  Contains the core functions to manage tasks, including adding, updating, deleting, and listing tasks. Tasks are stored in a JSON file.

- **colourOutput.py:**  
  Defines ANSI escape codes for color output in the terminal (Orange/Yellow for _in-progress_, Green for _done_).

- **tasks.json:**  
  A JSON file that stores the list of tasks. Initially, it should contain an empty JSON array:
  ```json
  []
  ```

---

## Installation

1. **Clone the repository** (or download the code files):
   ```bash
   git clone https://github.com/yourusername/task-manager-cli.git
   cd task-manager-cli
   ```
2. **Ensure Python is installed**
    ```bash
    python --version
    ```
3. **(Optional) Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

---

## Usage

1. **Run the application**
    ```bash
    python main.py
    ```

2. **Follow the on-screen promts:**
    * 1: Add Task
    * 2: Edit Task Description
    * 3: Update Task Status
    * 4: Delete Task
    * 5: List Tasks

3. **Follow the on-screen promts:**
    * Adding a Task: Choose option 1 and enter a task description when prompted.
    * Editing a Task Description: Choose option 2, select a task by its ID, and enter the new description.
    * Updating Task Status: Choose option 3 to toggle the status of a task between in-progress and done.
    * Deleting a Task: Choose option 4 and provide the task ID you wish to delete. Press 0 to cancel.
    * Listing Tasks: Choose option 5 to view tasks, with filters for all tasks, tasks in-progress, or tasks done.

---

## Dependencies

This project uses only Python's standard libraries:
 * json
 * datetime
 * os

No additional installation is required beyond having Python 3.x installed.