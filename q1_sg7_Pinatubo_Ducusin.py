class Glassware:
    def __init__(self, material="Glass"):
        self.material = material

class Beaker(Glassware):
    def __init__(self, material="Glass"):
        self.material = material

class Tray:
    def __init__(self):
        self.beakers = []
        for i in range(5):
            self.beakers.append(Beaker())

if __name__ == "__main__":
    tray = Tray()
    print(f"Tray created with {len(tray.beakers)} beakers.")
    
my_tray = Tray()   
del tray
