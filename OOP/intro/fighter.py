import time

class Fighter:
    def __init__(self, name, age, weapon, ability, strength, weight, speed):
        #name, age, weapon, ability, strength, weight, speed, percent
        print("running the fighter constructor!")
        self.name = name
        self.age = age
        self.ability = ability
        self.weapon = weapon
        self.strength = strength
        self.weight = weight
        self.speed = speed
        self.percent = 0
        self.shielding = False
    def print_status(self):
        print(f"name: {self.name}")
        print(f"percent: {self.percent}")
        print(f"ability: {self.ability}")
        print(f"strength: {self.strength}")
        print(f"weight: {self.weight}")
        print(f"speed: {self.speed}")
    def shield(self):
        self.shielding = True
        print(f"{self.name} has put up their shield!")
    def attack(self, opponent):
        if(opponent.shielding):
            print(f"{self.name} attacked {opponent.name}, but the shield blocked it!!!")
            opponent.shielding = False
        else:
            damage = 6
            opponent.percent += damage
            print(f"{self.name} attacked {opponent.name} and dealt {damage}%!!!")
    def special(self, opponent):
        if(opponent.shielding):
            print(f"{self.name} performed a special on {opponent.name}, but the shield blocked it!!!")
            opponent.shielding = False
        else:
            damage = 15
            opponent.percent += damage
            print(f"{self.name} performed a special move on {opponent.name} and dealt {damage}%!!!")

class Samus(Fighter):
    def __init__(self):
        print("calling the samus constructor!")
        super().__init__("Samus",29,"arm cannon","curl up in a ball",8,8,4)
        self.charged = False
    def special(self, opponent):
        if(self.charged):
            self.charged = False
            if(opponent.shielding):
                print(f"{self.name} fired her laser at {opponent.name}, but the shield blocked it!!!")
                opponent.shielding = False
            else:
                damage = 32
                opponent.percent += damage
                print(f"{self.name} fired her laser at {opponent.name} and dealt {damage}%!!!")
        else:
            self.charged = True
            print(f"{self.name} is charging up her arm cannon!")

class CaptainFalcon(Fighter):
    def __init__(self):
        super().__init__("Captain Falcon", 42, "fists", "falcon punch",8,7,8)
    def special(self, opponent):
        print("falcon...")
        time.sleep(3)
        if(opponent.shielding):
            print(f"PAaaauuuneweoij oof. It was blocked by {opponent.name}")
            opponent.shielding = False
        else:
            damage = 20
            opponent.percent += damage
            print(f"PAWNCH!!!{opponent.name} has been REKT and took {damage}%!!!")
    
class Lucario(Fighter):
    def __init__(self):
        super().__init__("Lucario",3,"aura","blue maic stuff",4,5,5)
        self.scaling = 1.0
    def assess_scaling(self):
        if(self.percent > 100):
            self.scaling = 2.5
        elif(self.percent > 80):
            self.scaling = 2
        elif(self.percent > 60):
            self.scaling = 1.75
        elif(self.percent > 40):
            self.scaling = 1.5
        else:
            self.scaling = 1.0
    def attack(self, opponent):
        self.assess_scaling()
        if(opponent.shielding):
            print(f"{self.name} attacked {opponent.name}, but the shield blocked it!!!")
            opponent.shielding = False
        else:
            damage = 6 * self.scaling
            opponent.percent += damage
            print(f"{self.name} attacked {opponent.name} and dealt {damage}%!!!")
    def special(self, opponent):
        self.assess_scaling()
        if(opponent.shielding):
            print(f"{self.name} performed a special on {opponent.name}, but the shield blocked it!!!")
            opponent.shielding = False
        else:
            damage = 15 * self.scaling
            opponent.percent += damage
            print(f"{self.name} performed a special move on {opponent.name} and dealt {damage}%!!!")



# samus = Samus()
# link = Fighter("Link",17,"sword","adventurer tools",6,6,6)
# samus.special(link)
# link.shield()
# samus.special(link)
falcon = CaptainFalcon()
lucario = Lucario()

lucario.attack(falcon)
falcon.print_status()

falcon.special(lucario)
falcon.special(lucario)
falcon.attack(lucario)
lucario.special(falcon)