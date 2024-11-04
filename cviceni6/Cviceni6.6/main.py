def create_task_list():
    """
    Creates task list using closure. Its create one list of tasks with two properties (description, is_complete) and some functions for manipulate it.

    :return: Dictionary with closure functions
    """

    tasks = []

    def add_task(description: str):
        """
        Add new uncompleted task
        :param description: the task text
        """
        if len(description.strip()) <= 0:
            raise Exception("Task must contains one char at least.")

        tasks.append({"description": description, "is_complete": False})

    def complete_task(description: str):
        """
        Mark a task as completed
        :param description: the task text
        """
        for t in tasks:
            if t["description"] == description:
                t["is_complete"] = True
                return
        raise Exception("Task not found.")

    def get_uncompleted():
        """
        Select uncompleted tasks and return it
        :return: list of descriptions in str
        """
        uncompleted = []
        for t in tasks:
            if not t["is_complete"]:
                uncompleted.append(t["description"])
        return uncompleted

    def get_completed():
        """
        Select completed tasks and return it
        :return: list of descriptions in str
        """
        completed = []
        for t in tasks:
            if t["is_complete"]:
                completed.append(t["description"])
        return completed

    def get_all_tasks():
        """
        Get all tasks with their completion status
        :return: list of descriptions in str with status
        """
        all_tasks = []
        for t in tasks:
            status = "[ X ]" if t["is_complete"] else "[   ]"
            all_tasks.append(f"{status} {t['description']}")
        return all_tasks

    return {
        "add_task": add_task,
        "complete_task": complete_task,
        "get_uncompleted": get_uncompleted,
        "get_completed": get_completed,
        "get_all_tasks": get_all_tasks
    }


peter_todo = create_task_list()
peter_todo["add_task"]("Vynest smeti")
peter_todo["add_task"]("Uklidit si pokojicek")
peter_todo["add_task"]("Uvarit veceri")
peter_todo["complete_task"]("Vynest smeti")

print("Uncompleted tasks:", peter_todo["get_uncompleted"]())
print("Completed tasks:", peter_todo["get_completed"]())
print("All tasks:", peter_todo["get_all_tasks"]())