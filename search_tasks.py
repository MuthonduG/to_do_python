class Searchtasks:
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