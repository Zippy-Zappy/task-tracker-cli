import sys
from task import Task

def main(filename):
    task = Task()

    if len(sys.argv) < 2:
        print("Incorrect usage. Correct usage is 'python [program file] [command]'")
        sys.exit()


    commands = {
        "add": lambda: (print
                        (task.create(filename, sys.argv[2]))
                        if len(sys.argv) == 3
                        else
                        print
                        ("Incorrect usage. Usage is 'python [program file] add [description]'")),

        "update": lambda: (print
                        (task.update(filename, int(sys.argv[2]), sys.argv[3]))
                        if len(sys.argv) == 4
                        else
                        print
                        ("Incorrect usage. Usage is 'python [program file] update [id] [description]'")),

        "delete": lambda: (print
                        (task.delete(filename, int(sys.argv[2])))
                        if len(sys.argv) == 3
                        else
                        print
                        ("Incorrect usage. Usage is 'python [program file] delete [id]'")),

        "list": lambda: (print
                        (task.list_tasks(filename, sys.argv[2]))
                        if len(sys.argv) == 3
                        else
                        print
                        (task.list_tasks(filename))),

        "mark-todo": lambda: (print
                        (task.change_status(filename, int(sys.argv[2], "todo"))
                        if len(sys.argv) == 3
                        else
                        print
                        ("Incorrect usage. Usage is 'python [program file] mark-todo [id]'"))),

        "mark-in-progress": lambda: (print
                        (task.change_status(filename, int(sys.argv[2]), "in-progress"))
                        if len(sys.argv) == 3
                        else
                        print
                        ("Incorrect usage. Usage is 'python [program file] mark-in-progress [id]'")),

        "mark-done": lambda: (print
                        (task.change_status(filename, int(sys.argv[2]), "done"))
                        if len(sys.argv) == 3
                        else
                        print
                        ("Incorrect usage. Usage is 'python [program file] mark-done [id]'"))
    }

    command = sys.argv[1]

    if command in commands:
        try:
            commands[command]()
        except Exception as ex:
            print(f"Error: {ex}")
    else:
        print("Unknown command. List of available commands: \n" + "\n".join(commands.keys()))

if __name__ == "__main__":
    FILENAME = "tracker.json"
    main(FILENAME)
