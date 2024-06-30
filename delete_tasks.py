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

# Initialize a class for managing tasks
class Deletetasks:
    def __init__(self, tasks):
        self.tasks = tasks
        
    def search_tasks(self, search_term):
        # Initialize results to store the tasks the user searched for
        results = []

        # Check if there are tasks within the existing list of tasks
        for task in self.tasks:
            # Check if user search term matches the task title
            if search_term in task['title']:
                # Append the searched-for task to results
                results.append(task)
        return results
    
    def delete_task(self):
        task_title = input("Enter task title to delete: \n") 
        results = self.search_tasks(task_title)

        if results:
            for task in results:
                self.tasks.remove(task)

            # Save the modified data back to the JSON file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print("Task(s) deleted successfully!")
        else:
            print("Task not found.")

# Create an instance of Deletetasks with the loaded data
delete_tasks_instance = Deletetasks(data['tasks'])

# Call the delete_task method to perform the deletion
delete_tasks_instance.delete_task()
