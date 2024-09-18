# Task Tracker CLI

Creating projects from Developer Roadmps. This one uses Python. Find this project and more here: https://roadmap.sh/projects/task-tracker 
This is a reupload to Github from my Gitlab repository: https://gitlab.com/ZippyZappy/task-tracker-cli
## Getting started

1. This project requires having at least the version 3 of Python installed.
2. This project is handled completely from a terminal. For example, the "cmd" windows terminal, the powershell terminal, or the Visual Studio terminal work just fine.

## Usage

1. Clone this repository.
2. Open your terminal. 
3. Go to the repositoriy's directory and write "python task.cli_py [commands]" - The following commands are available:
    - **add**: creates a task and adds it to the list. For example: `python task_cli.py add "Buy groceries"`
    - **update**: updates the description of a task. It needs a numeric id. For example: `python task_cli.py update [id] "Buy groceries and cook dinner"`
    - **delete**: deletes a task forever. It needs a numeric id. For example: `python task_cli.py delete [id]`
    - **list**: it lists all available. For example: `python task_cli.py list`. You can optionally choose which tasks you want to see, depending on their status. For example, `python task_cli.py list in-progress` will list all taks with the "in-progress" status.
    - **mark-todo**: changes the status of a task to "todo." For example: `python task_cli.py mark-todo [id]`
    - **mark-in-progress**: changes the status of a task to "in-progress."
    - **mark-done**: changes the status of a task to "done"
