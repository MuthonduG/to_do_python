import json

# Define JSON file path
file_path = "tasks.json"

class Edittasks:
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
    
    def edit_tasks(self):
        task_title = input("Enter task title to edit: \n") 
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
                    json.dump({"tasks": self.tasks}, file, indent=4)
            print("Task(s) edited successfully!")
        else:
            print("Task not found.")
