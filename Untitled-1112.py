class Car:
    def __init__(self, engine):
        self.engine = engine

class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

myCar=Car(GasEngine(4))
myCar.engine.start()
myCar=Car(DieselEngine(2))
myCar.engine.start()