class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def getBrand(self):
        return self.brand
    
    def getModel(self):
        return self.model
    
    def setBrand(self, brand):
        self.brand = brand

    def setModel(self, model):
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.gas = 'Petrol'
        self.wheel = 4

    def setWheel(self, wheel):
        self.wheel = wheel

    def getWheel(self):
        return self.wheel

    def sound(self):
        return 'beep beep beep'

    def getInfo(self):
        print(
            '\n brand:', self.getBrand(), 
            '\n model:', self.getModel(), 
            '\n sound:', self.sound(), 
            '\n gas:', self.gas,
            '\n wheel:', self.getWheel()
            )


class Bike(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.gas = 'kerisene'

    def sound(self):
        return 'Honk honk honk'

   
benz = Car('Mercedes Benz', 'C300')
benz.getInfo()

lexus = Car('lexus', 'SL300')
lexus.getInfo()

honda = Bike('Honda', '6300')
honda.setWheel(2)
honda.getInfo()

benz.setModel('G-Wagon')
benz.setWheel(6)
benz.getInfo()

