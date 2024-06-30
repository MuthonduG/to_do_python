# Initialize a class for viewing tasks
class Viewtasks:

    def __init__(self, tasks):
        self.tasks = tasks

    # Initialize a method for searching
    def search_tasks(self, search_term):
        # Initialize a results to store the task[s] the user searched for
        results = []

        # Check if there are tasks within the existing list of tasks
        for task in self.tasks:
            # check if user search term can search by date or title
            if search_term in task['date'] or search_term in task['title']:
                # Append the searched for task in resulsts
                results.append(task)
        return results

    # Initialize a method to view searched for tasks
    def view_tasks(self):
        # Reques user to search for tasks by either title or date
        view_choice = input("Search by date format (YYYY-MM-DD) or title: \n")
        # initialize results and store data from calling search_tasks method 
        results = self.search_tasks(view_choice)

        # If results is not null, display the data
        if results:
            for task in results:
                print(f"Date: {task['date']}, Title: {task['title']}, Description: {task['description']}")
        else:
            print("No tasks found.")

