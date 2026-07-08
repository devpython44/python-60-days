# user = {
#     "name": "Artem",
#     "age": 14,
#     "language": "Python",
#     "github": "devpython44"
# }

# print(user["name"])
# print(user["age"])
# print(user["language"])
# print(user["github"])

# tasks = [
#     {
#         "name": "Купить хлеб",
#         "done": False
#     },
#     {
#         "name": "Выучить Python",
#         "done": True
#     }
# ]

# print(tasks[0]["name"])
# print(tasks[1]["done"])

# user = {
#     "name": "Artem",
#     "age": 14,
#     "github": "devpython44",
#     "city": "Dnipro"
# }
# user["age"] = 15
# print(user)


user = {
    "name": "Artem",
    "age": 15
}

print(user.get("age", 0))
print(user.get("city", "Не указан"))