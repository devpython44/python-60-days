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

wolf = {
    "name": "Волк",
    "hp": 25,
    "damage": 18,
    "gold": 20,
    "xp": 20
}

goblin = {
    "name": "Гоблин",
    "hp": 15,
    "damage": 8,
    "gold": 15,
    "xp": 15
}

orc = {
    "name": "Орк",
    "hp": 40,
    "damage": 25,
    "gold": 40,
    "xp": 40
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

def fight_enemy():
    enemies = [wolf, goblin, orc]
    enemy = random.choice(enemies).copy()
    print(f"\nТебе встретился {enemy['name']}!\n")
    
    while player["hp"] > 0 and enemy["hp"] > 0:
        enemy["hp"] -= player["damage"]
        print(f"Ты ударил {enemy['name']} на {player['damage']} урона!")
        print(f"HP {enemy['name']}: {enemy['hp']}")
        if enemy["hp"] <= 0:
            player["gold"] += enemy["gold"]
            player["xp"] += enemy["xp"]
            save_player()
            
            print(f"""Ты победил {enemy['name']}!
            Ты получил {enemy['gold']} золота!
            Ты получил {enemy['xp']} опыта!""")

            break
        player["hp"] -= enemy["damage"]
        save_player()
        print(f"{enemy['name']} ударил тебя на {enemy['damage']} урона!")
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

def shop():
    while True:
        print("""
    === Магазин ===    
        
    1. Зелье лечения (+20 HP) - 20 золота
    2. Улучшить урон (+5) - 50 золота
    3. Выход
    """)
        choice = input("Выбор: ")
        
        if choice == "1":
            if player["gold"] >= 20:
                player["gold"] -= 20
                player["hp"] += 20
                save_player()
                
                print("Зелье применено!")
            else:
                print("Недостаточно золота!")
                
        elif choice == "2":
            if player["gold"] >= 50:
                player["gold"] -= 50
                player["damage"] += 5
                save_player()
                
                print("Урон улучшен!")
            else:
                print("Недостаточно золота!")    
                
        elif choice == "3":
            break

        else:
            print("Ввод некоректный!")

# def show_enemy(enemy):
#     print(enemy["name"])
#     print(enemy["hp"])
#     print(enemy["damage"])

menu = """
=== RPG ===

1. Показать героя
2. Исследовать лес
3. Бой
4. Магазин
5. Выход
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
        fight_enemy()
        
    elif choice == "4":
        shop()
    
    elif choice == "5":
        save_player()
        print("Пока")
        break

    else:
        print("Ввод некоректный!")
