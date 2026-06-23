class Duck():
    def walk (self):
        print("鴨子在走路")
    def talk(self):
        print("鴨子鴨鴨叫")
class Frog():
    def walk (self):
        print("青蛙在走路")
    def talk(self):
        print("青蛙呱呱叫")

class Person():
    def catch(self,animal):
        animal.walk()
        animal.talk()       

duck=Duck()
frog=Frog()
player=Person()
player.catch(frog)

