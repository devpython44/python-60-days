import json

tasks = [
    "Купить хлеб",
    "Выучить Python",
    "Сделать проект"
]

with open("tasks.json", "w") as file:
    json.dump(tasks, file)
    
with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)
    
print(loaded_tasks)
