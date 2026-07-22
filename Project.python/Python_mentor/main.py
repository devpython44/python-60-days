import tkinter as tk


# ==========================
# КЛАССЫ
# ==========================

class Lesson:
    def __init__(self, title, theory):
        self.title = title
        self.theory = theory
        self.tasks = []

class Task:
    def __init__(self, question, hint):
        self.question = question
        self.hint = hint


# ==========================
# ДАННЫЕ (уроки)
# ==========================

task1 = Task(
    "Напиши функцию, которая возвращает квадрат числа.",
    "Используй return"
)

task2 = Task(
    "Напиши функцию, которая возвращает сумму двух чисел.",
    "Используй два параметра."
)

lesson_functions = Lesson(
    "Функции",
    """
Функция — это блок кода,
который можно вызывать много раз.

Пример:

def hello():
    print("Привет")
"""
)

lesson_functions.tasks.append(task1)
lesson_functions.tasks.append(task2)

lesson_lists = Lesson(
    "Списки",
    """
Список хранит несколько значений.

numbers = [1, 2, 3]
"""
)


# ==========================
# ФУНКЦИИ
# ==========================

def show_theory():
    theory_label.config(
        text=lesson_functions.theory
    )

def show_lists():
    theory_label.config(
        text=lesson_lists.theory
    )

def show_task():
    task_label.config(
        text=lesson_functions.tasks[0].question
    )


# ==========================
# СОЗДАНИЕ ОКНА
# ==========================

window = tk.Tk()
window.title("Python Mentor")
window.geometry("600x400")


# ==========================
# ВИДЖЕТЫ
# ==========================

title = tk.Label(
    window,
    text="Python Mentor",
    font=("Arial", 20)
)

button_functions = tk.Button(
    window,
    text="Функции",
    command=show_theory
)

button_lists = tk.Button(
    window,
    text="Списки",
    command=show_lists
)

button_task = tk.Button(
    window,
    text="Получить задачу",
    command=show_task
)

theory_label = tk.Label(
    window,
    text="Выбери тему",
    wraplength=500,
    justify="left"
)

task_label = tk.Label(
    window,
    text="",
    wraplength=500,
    justify="left"
)

# ==========================
# РАЗМЕЩЕНИЕ ВИДЖЕТОВ
# ==========================

title.pack(pady=20)
button_functions.pack()
button_lists.pack()
button_task.pack()
theory_label.pack(pady=20)
task_label.pack(pady=10)

# ==========================
# ЗАПУСК ПРОГРАММЫ
# ==========================

window.mainloop()
