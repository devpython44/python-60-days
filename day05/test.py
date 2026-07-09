# task = input("Введите задачу: ")

# tasks.append({
#     "name", task,
#     "done", False
# })

tasks = [
    {
        "name": "Купить хлеб",
        "done": False
    }
]

tasks[0]["done"] = True

if tasks[0]["done"] == True:
    print("[Выполнено]")
else:
    print("[не выполнено]")
    
print(tasks)
