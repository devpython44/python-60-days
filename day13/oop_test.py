class Lesson:
    def __init__(self, title, theory):
        self.title = title
        self.theory = theory
        self.tasks = []
       
class Task:
    def __init__(self, question, hint):
        self.question = question
        self.hint = hint

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

for task in lesson_functions.tasks:
    print(task.question)

# print(lesson_functions.title)
# print(lesson_functions.theory)

# print(task1.question)
# print(task1.hint)
