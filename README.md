

# Task Tracker CLI https://roadmap.sh/projects/task-tracker

Task Tracker CLI is a simple command-line application designed to help you track, manage, and organize your tasks. It stores tasks in a JSON file and allows you to interact with them using various commands. This project will help you practice programming, including working with files, handling user inputs, and building a CLI application.

## Features

This CLI application provides the following functionality:

- **Add a Task**: Add a new task with a description.
- **Update a Task**: Update an existing task's description.
- **Delete a Task**: Delete a task based on its ID.
- **Mark a Task as In Progress or Done**: Change the status of a task.
- **List All Tasks**: Display all tasks.
- **List Tasks by Status**: Filter tasks by their status (`done`, `todo`, `in-progress`).

## Requirements

- The application runs from the command line and accepts actions and inputs as arguments.
- The tasks are stored in a JSON file in the current directory. If the file does not exist, it will be created automatically.
- The application should handle the following tasks:
  - Add, update, and delete tasks
  - Mark tasks as in progress or done
  - List all tasks
  - List tasks based on their status (`done`, `todo`, `in-progress`)

## Task Properties

Each task contains the following properties:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## Installation

1. Clone the repository or download the files.
2. Ensure Python (3.6 or higher) is installed on your system.
3. Navigate to the project directory:

   ```bash
   cd task-tracker-cli
   ```

4. The project does not require any external libraries.

## Usage

### Commands

You can execute the following commands:

1. **Add a Task**

   To add a new task, run:

   ```bash
   python task_tracker.py add "Buy groceries"
   ```

   This will add a new task with the description "Buy groceries".

2. **Update a Task**

   To update an existing task's description, run:

   ```bash
   python task_tracker.py update <task_id> "New description"
   ```

   Replace `<task_id>` with the task's ID and provide the new description.

3. **Delete a Task**

   To delete a task, run:

   ```bash
   python task_tracker.py delete <task_id>
   ```

   Replace `<task_id>` with the task's ID.

4. **Mark a Task as In Progress**

   To mark a task as in progress, run:

   ```bash
   python task_tracker.py mark-in-progress <task_id>
   ```

5. **Mark a Task as Done**

   To mark a task as done, run:

   ```bash
   python task_tracker.py mark-done <task_id>
   ```

6. **List All Tasks**

   To list all tasks, run:

   ```bash
   python task_tracker.py list
   ```

7. **List Tasks by Status**

   To list tasks by their status (`done`, `todo`, or `in-progress`), run:

   ```bash
   python task_tracker.py list done
   python task_tracker.py list todo
   python task_tracker.py list in-progress
   ```

## Example Usage

```bash
# Add a task
python task_tracker.py add "Prepare for Monday's meeting"

# Update a task
python task_tracker.py update 1 "Prepare for Monday's meeting with the quarterly report"

# Mark the task as in progress
python task_tracker.py mark-in-progress 1

# Mark the task as done
python task_tracker.py mark-done 1

# List all tasks
python task_tracker.py list

# List tasks by status
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Project Structure

```
task-tracker-cli/
│
├── task_tracker.py         # Main application file
└── tasks.json              # JSON file to store tasks (automatically created)
```

## Error Handling

The application gracefully handles the following errors:

- **Missing or empty JSON file**: The program will create the file if it doesn't exist.
- **Invalid Task ID**: If you try to update, delete, or mark a task with an invalid ID, the program will notify you that the task was not found.
- **Invalid Command or Arguments**: If the user provides incorrect arguments or commands, the program will display an error message and suggest the correct syntax.

## Contributing

Feel free to contribute! You can open an issue if you encounter any bugs or want to suggest new features. Pull requests are also welcome.

## License 

This project is free to use and modify. You can use it for personal or educational purposes.

