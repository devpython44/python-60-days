class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def show(self):
        print(self.name)
        print(self.hp)
        print(self.damage)
        
player = Player("Artem", 100, 10)


player.show()