class Hero:

    def __init__(self, name, HP):
      self.name = name
      self.hp = HP
    def take_damage(self, amount):
      self.hp -= amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"{arthur.name} took damage!")
print("")

print(f"{arthur.name}'s Remaining HP : {arthur.hp}")
print(f"{morgana.name}'s Remaining HP : {morgana.hp}")
