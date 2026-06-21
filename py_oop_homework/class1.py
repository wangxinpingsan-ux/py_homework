class Pokemon ():
    
    def __init__(self,species):
        self.species=species
    def attack(self):
        print("神奇寶貝發動了普通攻擊！")
        
class Pikachu (Pokemon):
    def attack(self):
        print("皮卡丘使用了十萬伏特！⚡")

player1=Pokemon("寶可夢")
print(player1.species)
player1.attack()

player2=Pikachu("寶可夢")
print(player2.species)
player2.attack()

