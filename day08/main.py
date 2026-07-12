import random
import json

player = {
    "name": "Artem",
    "level": 1,
    "xp": 0,
    "hp": 100,
    "gold": 0,
    "damage": 10
}

def show_player():
    print("=== Герой ===")
    print(f"Имя: {player['name']}")
    print(f"Уровень: {player['level']}")
    print(f"Опыт: {player['xp']}")
    print(f"HP: {player['hp']}")
    print(f"Золото: {player['gold']}")
    print(f"Урон: {player['damage']}")

def explore_forest():
    event = random.randint(1,2)
    if event == 1:
        player["gold"] += 10
        player["xp"] += 20
        save_player()
        print("Ты получил 20 опыта!")
        print("Ты нашёл 10 золота!")
        if player["xp"] >= 100:
            player["level"] += 1
            player["xp"] -= 100
            player["hp"] += 20
            player["damage"] += 5
            save_player()
            print("Новый уровень!")
            print(f"Теперь твой уровень: {player['level']}")
    else:
        player["hp"] -= 15
        print("На тебя напал волк!\nТы потерял 15 HP!")
        if player["hp"] <= 0:
            print("Ты погиб!")

def fight_wolf():
    wolf = {
        "name": "Волк",
        "hp": 30,
        "damage": 15
    }

    while player["hp"] > 0 and wolf["hp"] > 0:
        wolf["hp"] -= player["damage"]
        print(f"Ты ударил волка на {player['damage']} урона!")
        print(f"HP волка: {wolf['hp']}")
        if wolf["hp"] <= 0:
            player["gold"] += 20
            player["xp"] += 20
            save_player()
            
            print("Ты победил волка!")
            print("Ты получил 20 золота!")
            print("Ты получил 20 опыта!")

            break
        player["hp"] -= wolf["damage"]
        save_player()
        print(f"Волк ударил тебя на {wolf['damage']} урона!")
        print(f"Твой HP: {player['hp']}")
        
        
        if player["hp"] <= 0:
            print("Ты погиб!")
            break

def save_player(): 
    with open("player.json", "w", encoding="utf-8") as file:
        json.dump(player, file, ensure_ascii=False, indent=4)
        
def load_player():
    global player
    
    try:
        with open("player.json", "r", encoding="utf-8") as file:
            player = json.load(file)
            
            print("Сохранение загружено!")
            
    except FileNotFoundError:
        print("Сохранение не найдено. Создан новый герой.")

menu = """
=== RPG ===

1. Показать героя
2. Исследовать лес
3. Бой с волком
4. Выход
"""

load_player()
while True:
    print(menu)
    choice = input("Выбор: ")
    
    if choice == "1":
        show_player()
        
    elif choice == "2":
        explore_forest()
        
    elif choice == "3":
        fight_wolf()
    
    elif choice == "4":
        save_player()
        print("Пока")
        break

    else:
        print("Ввод некоректный!")
