import argparse
import json
import os
import datetime

# Nom du fichier JSON où seront stockées les tâches
TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []



def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def generate_task_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1


def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_task_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")


def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if status is None or task["status"] == status]
    if not filtered_tasks:
        print("No tasks found.")
        return
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Commande pour ajouter une tâche
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # Commande pour mettre à jour une tâche
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="ID of the task")
    parser_update.add_argument("description", type=str, help="New description of the task")

    # Commande pour supprimer une tâche
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task")

    # Commande pour marquer une tâche comme en cours
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    parser_mark_in_progress.add_argument("id", type=int, help="ID of the task")

    # Commande pour marquer une tâche comme effectuée
    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="ID of the task")

    # Commande pour lister les tâches
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"], help="Status filter")

    # Parsing des arguments
    args = parser.parse_args()

    # Exécution des commandes en fonction de l'argument "command"
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_task(args.id, "in-progress")
    elif args.command == "mark-done":
        mark_task(args.id, "done")
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
