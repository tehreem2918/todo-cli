import json
from pathlib import Path

FILE = Path("tasks.json")  # tasks are saved here


def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return []


def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2))


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")


def main():
    tasks = load_tasks()
    while True:
        print("\n1) View  2) Add  3) Complete  4) Delete  5) Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
        elif choice in ("3", "4"):
            show_tasks(tasks)
            try:
                num = int(input("Task number: "))
                if not 1 <= num <= len(tasks):
                    raise IndexError
                if choice == "3":
                    tasks[num - 1]["done"] = True
                else:
                    tasks.pop(num - 1)
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Invalid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1-5.")


if __name__ == "__main__":
    main()