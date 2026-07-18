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
        # Это розобраться потом!!!
        # lesson_functions.tasks.append(task1)
    )

def show_lists():
    theory_label.config(
        text=lesson_lists.theory
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

theory_label = tk.Label(
    window,
    text="Выбери тему",
    wraplength=500,
    justify="left"
)


# ==========================
# РАЗМЕЩЕНИЕ ВИДЖЕТОВ
# ==========================

title.pack(pady=20)
button_functions.pack()
button_lists.pack()
theory_label.pack(pady=20)

# ==========================
# ЗАПУСК ПРОГРАММЫ
# ==========================

window.mainloop()
