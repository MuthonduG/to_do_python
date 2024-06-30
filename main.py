from load_json import load_data
from add_tasks import AddTasks
from view_tasks import Viewtasks
from edit_tasks import Edittasks
from delete_tasks import Deletetasks

data = load_data()

class Managetasks:
    def __init__(self, tasks):
        self.tasks = tasks
    
    def decision_block(self):
        while True:
            try:
                user_decision = int(input("Enter (1) for adding task[s], (2) for viewing task[s], (3) for deleting task[s], (4) for editing task[s], (5) to exit: "))

                if user_decision < 1 or user_decision > 5:
                    print("Input must be a value between 1 and 5")
                else:
                    if user_decision == 1:
                        try:
                            num_tasks = int(input("Enter number of tasks you want to add: \n"))
                            add_new_tasks = AddTasks(self.tasks)
                            add_new_tasks.create_new_tasks(num_tasks)
                        except ValueError:
                            print("Input must be an integer!!!")

                    elif user_decision == 2:
                        view_tasks = Viewtasks(self.tasks)
                        view_tasks.view_tasks()

                    elif user_decision == 3:
                        delete_tasks = Deletetasks(self.tasks)
                        delete_tasks.delete_task()

                    elif user_decision == 4:
                        edit_tasks = Edittasks(self.tasks)
                        edit_tasks.edit_tasks()
                        
                    elif user_decision == 5:
                        break
            except ValueError:
                print("Input must be an integer!!!")

# Create an instance of Managetasks with the loaded data and start the decision block
manage_tasks_instance = Managetasks(data['tasks'])
manage_tasks_instance.decision_block()
