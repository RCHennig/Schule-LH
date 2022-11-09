class Car:
    'Simple caR.'
    def __init__(self, brand, price, hp, fuel, mileage, color, noaccident):
        'Atributes'
        self.brand = brand
        self.price = price
        self.hp = hp
        self.fuel = fuel
        self.mileage = mileage
        self.color = color
        self.noaccident = noaccident

    def info(self):
        print("Brand:", self.brand)
        print("Price:", self.price, "€")
        print("Horsepower:", self.hp)
        print("Fuel-type:", self.fuel)
        print("Mileage:", self.mileage, "KM")
        print("Color:", self.color)
        if self.noaccident:
            print("Unfallfrei")


car1 = Car(brand="Ford", price="7999.99", hp="101", fuel="Diesel", mileage="125000",
           color="silber metallic", noaccident=True)

print(car1.info())
