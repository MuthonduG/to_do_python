# simple to_do_python app ##
This project is a simple to-do list application that allows users to manage their tasks. The application covers fundamental Python concepts such as data structures, loops, and basic user input/output. Users can add, view, and remove tasks, and the application supports saving and loading tasks to/from a file.

## Features ##
1. Add Task: Allows users to add tasks to the to-do list. Each task includes a name and a due date.
2. View Tasks: Displays the list of tasks with their names and due dates.
3. Remove Task: Users can remove tasks from the list by specifying the task name.
4. Save/Load Tasks: Implements a way to save the to-do list to a file (e.g., a text file) and load it when the program starts.

## Usage ##
1. Load the To-Do List Application
The application will load the existing tasks from tasks.json when it starts. If the file is not found or is empty/invalid, it will initialize with an empty tasks list.

2. Add Task
To add a task, the user needs to provide:

Task Name
Due Date
The task will be added to the list and saved to tasks.json.

3. View Tasks
Displays the list of all tasks with their names and due dates.

4. Remove Task
To remove a task, the user needs to provide the task name. If the task is found, it will be removed from the list and the changes will be saved to tasks.json.

5. Save/Load Tasks
Tasks are automatically saved to tasks.json after adding or removing a task. When the program starts, it will load the tasks from tasks.json.
