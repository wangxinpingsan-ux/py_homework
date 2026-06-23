class Pikachu ():
    def __init__(self,name):
        self.name=name
        print(self.name)

    def eat(self):
        print("皮卡丘吃了一顆蘋果 🍎")
        return self
    def train(self):
        print("皮卡丘正在認真訓練 💪")
        return self
    def attack(self):
        print("皮卡丘使用了十萬伏特！⚡")
        return self

pika=Pikachu ("皮卡丘")
pika.eat().train().attack()