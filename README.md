# To-Do List Application

## Project Description

This is a simple to-do list application that allows users to add, view, edit, and remove tasks. The project demonstrates fundamental Python concepts such as data structures, loops, and basic user input/output.

## Features

- **Add Task**: Allows users to add tasks to the to-do list. Each task includes a title, description, due date, status, and timestamp.
- **View Tasks**: Displays the list of tasks with their details.
- **Edit Task**: Allows users to edit the details of existing tasks.
- **Remove Task**: Users can remove tasks from the list by specifying the task title.
- **Save/Load Tasks**: The application saves the to-do list to a JSON file (`tasks.json`) and loads it when the program starts.

## Project Structure

- `load_json.py`: Contains the function to load data from the JSON file.
- `add_tasks.py`: Contains the `AddTasks` class for adding tasks.
- `view_tasks.py`: Contains the `Viewtasks` class for viewing tasks.
- `edit_tasks.py`: Contains the `Edittasks` class for editing tasks.
- `delete_tasks.py`: Contains the `Deletetasks` class for deleting tasks.
- `main.py`: Contains the `Managetasks` class and the main menu-driven interface.

## Guidelines

- Use dictionaries or lists to store tasks with their attributes (name, description, due date, status, and timestamp).
- Implement a menu-driven interface where users can choose to add, view, edit, or remove tasks.
- Use functions to modularize your code (e.g., separate functions for adding, viewing, editing, and removing tasks).
- Implement error handling to ensure the program doesn't crash when the user enters incorrect input.
- Provide a clear and user-friendly interface with instructions for the user.

## How to Run the Project

1. Ensure all the project files (`load_json.py`, `add_tasks.py`, `view_tasks.py`, `edit_tasks.py`, `delete_tasks.py`, and `main.py`) are in the same directory.
2. Run `main.py` to start the application:

   ```bash
   python main.py
