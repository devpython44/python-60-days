import json

try:
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
        
except FileNotFoundError:
    tasks = []

def add_task():
    task = input("Введите задачу: ")
    tasks.append({
        "name": task,
        "done": False
    })
    save_tasks()
    print(f"Задача '{task}' добавлена!")

def show_tasks():
    if not tasks:
    # if len(tasks) == 0:
        print("Список задач пуст!")
    else:
        for i, task in enumerate(tasks, start=1):
            if task["done"] == True:
                status = "[✓]"
            else:
                status = "[ ]"
        
            print(f"{i}. {status} {task['name']}")

def delete_task():
    if not tasks:
    # if len(tasks) == 0:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']}")

        try:
            task_number = int(input("Введите номер задачи для удаления: "))
        except ValueError:
            print("Нужно ввести число!")
            return
            
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Задача '{deleted_task['name']}' удалена!")
        else:
            print("Такой задачи нет!")

def complete_task():
    if not tasks:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']}")
            
        try:
            task_number = int(input("Введите номер задачи: "))
            if 1 <= task_number <= len(tasks):
                
                if tasks[task_number - 1]["done"]:
                    print("Задача уже выполнена!")
                else:
                    tasks[task_number - 1]["done"] = True
                    save_tasks()
                    print("Задача отмечена как выполненная!")
            else:
                print("Такой задачи нет!")
        except ValueError:
            print("Нужно ввести число!")

def show_stats():
    total = len(tasks)
    completed = 0
    
    for task in tasks:
        if task["done"]:
            completed += 1
            
    remaining = total - completed
    print(f"""
=== Статистика ===
Всего задач: {total}
Выполнено: {completed}
Осталось: {remaining}""")
    
def search_tasks():
    query = input("Введите текст для поиска: ")
    found = False
    
    for i, task in enumerate(tasks, start=1):
        if query in task["name"]:
            found = True
            
            if task["done"]:
                status = "[✓]"
            else:
                status = "[ ]"
            
            print(f"{i}. {status} {task['name']}")
    if not found:
        print("Ничего не найдено!")
            
def edit_task():
    if not tasks:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']}")
        
        try:
            task_number = int(input("Введите номер задачи: "))
            
            if 1 <= task_number <= len(tasks):
                new_task = input("Введите новую задачу: ")
                tasks[task_number - 1]["name"] = new_task
                tasks[task_number - 1]["done"] = False
                save_tasks()
                print("Задача успешно изменена!")
                
            else:
                print("Такой задачи нет!")
                
        except ValueError:
            print("Нужно ввести число!")

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False)
        
menu = """
    ===MENU===
1. Добавить задачу
2. Показать задачи
3. Удалить задачу
4. Отметить выполненной
5. Статистика
6. Поиск задачи
7. Изменить задачу
8. Выход
"""

while True:
    print(menu)
    client_data = input("Ввод: ")
    
    if client_data == "1":
        add_task()
        
    elif client_data == "2":
        show_tasks()
        
    elif client_data == "3":
        delete_task()
        
    elif client_data == "4":
        complete_task()
        
    elif client_data == "5":
        show_stats()
        
    elif client_data == "6":
        search_tasks()
        
    elif client_data == "7":
        edit_task()
    
    elif client_data == "8":
        print("Пока)")
        break
    else:
        print("Такого пункта нет!")
