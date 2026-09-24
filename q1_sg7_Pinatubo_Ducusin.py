class Glassware:
    def __init__(self, material="Glass"):
        self.material = material

class Beaker(Glassware):
    def __init__(self, capacity_ml=250, material="Glass"):
        super().__init__(material)
        self.capacity_ml = capacity_ml

class Tray:
    def __init__(self, num_beakers=5):
        self.beakers = [Beaker() for _ in range(num_beakers)]

if __name__ == "__main__":
    tray = Tray()
    print(f"Tray created with {len(tray.beakers)} beakers.")
    
    del tray
