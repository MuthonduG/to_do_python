import json

# Define JSON file path
file_path = "tasks.json"

# Read JSON file and load it into a variable
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("File path not found or file is empty/invalid, initializing with an empty tasks list.")
    data = {"tasks": []}

# Initialize a class for viewing tasks
class Edittasks:
    def __init__(self, tasks):
        self.tasks = tasks
        
    def search_tasks(self, search_term):
        # Initialize a results to store the task[s] the user searched for
        results = []

        # Check if there are tasks within the existing list of tasks
        for task in self.tasks:
            # check if user search term can search by date or title
            if search_term in task['title']:
                # Append the searched for task in results
                results.append(task)
        return results
    
    def edit_tasks(self):
        task_title = input("Enter task title: \n") 
        results = self.search_tasks(task_title)

        if results:
            new_title = input("Enter new task title: \n") 
            new_description = input("Enter new task description: \n")
            new_deadline = input("Enter new task deadline: \n")

            for task in results:
                task['title'] = new_title
                task['description'] = new_description
                task['deadline'] = new_deadline

            # Save the modified data back to the JSON file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print("Task updated successfully!")
        else:
            print("Task not found.")

# Create an instance of Edittasks with the loaded data
edit_tasks_instance = Edittasks(data['tasks'])

# Call the edit_tasks method to perform the edit
edit_tasks_instance.edit_tasks()
