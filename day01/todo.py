tasks = []

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

            task_number = int(input("Введите номер задачи для удаления: "))
            
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Задача '{deleted_task}' удалена!")
            else:
                print("Такой задачи нет!")
    elif client_data == "4":
        print("Пока)")
        break
    else:
        print("Такого пункта нет!")
