import json

try:
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
        
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False)

menu = """
1. Добавить задачу
2. Показать задачи
3. Удалить задачу
4. Выход
"""

while True:
    print(menu)
    client_data = input("Ввод: ")
    
    if client_data == "1":
        task = input("Введите задачу: ")
        tasks.append(task)
        save_tasks()
        print(f"Задача '{task}' добавлена!")
        
    elif client_data == "2":
        if len(tasks) == 0:
            print("Список задач пуст")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                
    elif client_data == "3":
        if len(tasks) == 0:
            print("Список задач пуст")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_number = int(input("Введите номер задачи для удаления: "))
            except ValueError:
                print("Нужно ввести число!")
                continue
            
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                save_tasks()
                print(f"Задача '{deleted_task}' удалена!")
            else:
                print("Такой задачи нет!")
    elif client_data == "4":
        print("Пока)")
        break
    else:
        print("Такого пункта нет!")
