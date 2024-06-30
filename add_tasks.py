from datetime import datetime, date
import json

# Define JSON file path
file_path = "tasks.json"

# Initialize a class for adding tasks
class AddTasks:
    def __init__(self, tasks):
        self.tasks = tasks

    # Initialize a method for creating new tasks
    def create_new_tasks(self, num_tasks): 
        # Initialize count to keep track of the number tasks added
        count = 0
        while count < num_tasks:
            # Request user input for task
            task_title = input("Enter task title: \n")
            task_description = input("Enter task description: \n")
            deadline = input("Enter expected deadline: \n")
            status = "Pending"
            current_date = date.today()
            current_time = datetime.now()

            # Initialize variable for holding user input data
            new_task = {
                'id': len(self.tasks) + 1,
                'title': task_title,
                'description': task_description,
                'deadline': deadline,
                'status': status,
                'date': str(current_date), 
                'time': current_time.strftime("%H:%M:%S")
            }

            # Append the new task to already existing tasks
            self.tasks.append(new_task)

            # Add the task to the json file
            with open(file_path, 'w') as file:
                json.dump({"tasks": self.tasks}, file, indent=4)

            # Add one to count to keep track of the added tasks
            count += 1
