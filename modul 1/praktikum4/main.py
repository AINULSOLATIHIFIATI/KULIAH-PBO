class Hero:
    # class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    def siapa(self):
        return f"{self.name} memiliki power {self.power}"

    def healthUp(self, up):
        self.health += up
        
    def gethealth(self):
        return self.health
    
    # method baru dengan parameter dan return
    def attack(self, musuh):
        damage = self.power - musuh.armor
        if damage < 0:
            damage = 0  # supaya tidak negatif
        musuh.health -= damage
        return f"{self.name} menyerang {musuh.name} dengan damage {damage}"

# Membuat objek
hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Axe", 200, 15, 0)

# Memakai method
print(hero1.siapa())
hero1.armor = 10
print(f"Armor {hero1.name} = {hero1.armor}")
print(f"Jumlah hero = {Hero.jumlah}")
hero1.healthUp(20)
print(f"Health {hero1.name} = {hero1.gethealth()}")
print(f"Health {hero2.name} = {hero2.gethealth()}")

# Coba serangan
print(hero1.attack(hero2))
print(f"Health {hero2.name} sekarang = {hero2.gethealth()}")