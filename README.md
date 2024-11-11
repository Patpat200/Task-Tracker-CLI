Here's the README in English:

---

# Task Tracker CLI

Task Tracker CLI is a command-line application for managing tasks easily. The application stores tasks in a JSON file and allows you to add, update, delete, and change the status of tasks.

## Features

The application provides the following features:

1. **Add a Task**: Add a new task with a description.
2. **Update a Task**: Update the description of an existing task.
3. **Delete a Task**: Delete a task based on its ID.
4. **Mark a Task as In Progress or Done**: Change the status of a task.
5. **List Tasks**: Display all tasks, or filter tasks that are completed, pending, or in progress.

## Installation

1. Clone the repository or download the files.
2. Ensure Python is installed on your system (Python 3.6 or higher).
3. Navigate to the project directory:

   ```bash
   cd task-tracker-cli
   ```

## Usage

Commands are executed from the command line. Here’s how to use each feature:

### 1. Add a Task

```bash
python task_tracker.py add "Buy groceries"
```

### 2. Update a Task

```bash
python task_tracker.py update <task_id> "Buy groceries and cook dinner"
```

### 3. Delete a Task

```bash
python task_tracker.py delete <task_id>
```

### 4. Mark a Task as In Progress

```bash
python task_tracker.py mark-in-progress <task_id>
```

### 5. Mark a Task as Done

```bash
python task_tracker.py mark-done <task_id>
```

### 6. List Tasks

To list all tasks:

```bash
python task_tracker.py list
```

To list only completed, pending, or in-progress tasks:

```bash
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Task Structure

Each task is stored in the `tasks.json` file with the following properties:

- **id**: Unique identifier for the task.
- **description**: Description of the task.
- **status**: Status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: Date and time when the task was created.
- **updatedAt**: Date and time when the task was last updated.

## Example Usage

```bash
# Add a task
python task_tracker.py add "Prepare for Monday's meeting"
# Update the task
python task_tracker.py update 1 "Prepare for Monday's meeting with the quarterly report"
# Mark the task as in progress
python task_tracker.py mark-in-progress 1
# Mark the task as done
python task_tracker.py mark-done 1
# List all completed tasks
python task_tracker.py list done
```

## Project Structure

```
task-tracker-cli/
│
├── task_tracker.py         # Main application file
└── tasks.json              # JSON file to store tasks (automatically created)
```

## Error Handling

The program handles the following errors:
- **Empty or Missing JSON File**: Creates an empty file if it doesn’t exist.
- **Task ID Not Found**: Displays an error message if the ID is invalid.
- **Incorrect Commands**: Checks for incorrect commands or arguments and displays an error message.

## Contributing

Contributions are welcome! Feel free to open issues to discuss bugs or potential features, or to submit a pull request.

## License

This project is free to use and modify as needed.

