import json
import os
import argparse
from datetime import datetime


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump({"tasks": []}, f, ensure_ascii=False, indent=4)

    def _load_tasks(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_tasks(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_task(self, description):
        """Работа с json: добавляем значения в список по ключу 'add'"""
        data = self._load_tasks()

        if "tasks" not in data:
            data["tasks"] = []

        tasks = data["tasks"]

        new_task = {
            "id": len(tasks) + 1,
            "description": description,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(new_task)
        data["tasks"] = tasks
        self._save_tasks(data)
        return print(f"Добавлена задача: {description}")

    def list_task(self, status=None):
        data = self._load_tasks()
        tasks = data.get("tasks", [])
        if not tasks:
            return print("Список  пуст. Добавьте их через `add`.")

        filtered = [t for t in tasks if not status or t["status"] == status]
        if not filtered:
            return print("Нет задач с таким статусом.")

        for t in filtered:
            return print(f"[{t['id']}] ({t['status']}) {t['description']} — {t['created_at']}")

    def to_complete_task(self, task_id):
        data = self._load_tasks()
        for t in data["tasks"]:
            if t["id"] == task_id:
                if t["status"] == "completed":
                    return print("Задача уже выполнена.")
                if t["status"] == "pending":
                    t["status"] = "completed"
                    self._save_tasks(data)
                    return print(f"Статус задачи {task_id} поменялся на 'выполнена'.")


    def delete_task(self, task_id):
        data = self._load_tasks()
        tasks = [t for t in data["tasks"] if t["id"] != task_id]
        if len(tasks) == len(data["tasks"]):
            return print("Задача не найдена.")
        data["tasks"] = tasks
        self._save_tasks(data)
        return print(f"Задача {task_id} успешно удалена.")

    def operation(self, args):
        if args.command == "add":
            self.add_task(args.description)
        elif args.command == "list":
            self.list_task(status=args.status)
        elif args.command == "complete":
            self.to_complete_task(args.id)
        elif args.command == "delete":
            self.delete_task(args.id)
        else:
            print("Неизвестная команда, попробуйте что-то из этого: add, list, complete, delete.")

def main():
    parser = argparse.ArgumentParser(description="Эта программа создает список задач и отслеживает их выполнение")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Добавить задачу")
    add_parser.add_argument("description", type=str, help="Описание")

    # list
    list_parser = subparsers.add_parser("list", help="Показать список задач")
    list_parser.add_argument("--status", choices=["pending", "completed"], help="Фильтрует задачи по статусу")

    # complete
    complete_parser = subparsers.add_parser("complete", help="Отмечает задачу выполненной")
    complete_parser.add_argument("id", type=int, help="ID задачи")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Удаляет задачу")
    delete_parser.add_argument("id", type=int, help="ID задачи")

    args = parser.parse_args()
    manager = TaskManager()
    manager.operation(args)


if __name__ == "__main__":
    main()