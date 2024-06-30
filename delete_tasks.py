import json

# Define JSON file path
file_path = "tasks.json"

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
                json.dump({"tasks": self.tasks}, file, indent=4)
            print("Task(s) deleted successfully!")
        else:
            print("Task not found.")
