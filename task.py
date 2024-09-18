import datetime
import pathlib
from json_manager import Manager

class Task():
    list_status = ["todo", "in-progress", "done"]

    def __init__(self):
        pass

    def create(self, filename, description):
        if not pathlib.Path(filename).exists():
            Manager.create_tracker(filename)
        new_data = {
            "id": Manager.generate_id(filename),
            "description": description,
            "status": "todo",
            "createdAt": datetime.datetime.now().strftime("%c"),
            "updatedAt": datetime.datetime.now().strftime("%c")
        }

        Manager.json_append(filename, new_data)
        return "Task successfully created."

    def update(self, filename, id_task, description):
        data = Manager.json_load(filename)

        for elem in data:
            if elem.get("id") == id_task:
                elem["description"] = description
                elem["updatedAt"] = datetime.datetime.now().strftime("%c")
                Manager.json_write(filename, data)
                return f"Task {id_task} updated."
        return f"Error. No task with the id {id_task} exists."

    def change_status(self, filename, id_task, status):
        if status not in self.list_status:
            return "Error. Unknown status. Available statuses are: \n" + "\n".join(self.list_status)

        data = Manager.json_load(filename)

        for elem in data:
            if elem.get("id") == id_task:
                elem["status"] = status
                elem["updatedAt"] = datetime.datetime.now().strftime("%c")
                Manager.json_write(filename, data)
                return "Task status successfully changed."
        return f"Error. No task with the id {id_task} exists."

    def delete(self, filename, id_task):
        data = Manager.json_load(filename)
        new_data = [entry for entry in data if entry.get("id") != id_task]

        #json library in Python doesn't have a delete function per se,
        #so all the data must be rewritten, except for the one
        #to be deleted.
        Manager.json_write(filename, new_data)
        return "Task successfully deleted."

    def list_tasks(self, filename, status=""):
        data = Manager.json_load(filename)
        if len(data) == 0:
            return "No tasks available."
        if status != "":
            if status not in self.list_status:
                return f"Error. '{status}' is an unknown status. Available statuses are: \n" + "\n".join(self.list_status)
            list_data = [task for task in data if task.get("status") == status]
            if len(list_data) == 0:
                return f"No tasks with '{status}' status available."
            return Manager.json_pretty_print(list_data)

        return Manager.json_pretty_print(data)
