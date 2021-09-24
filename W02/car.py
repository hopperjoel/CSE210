class Car:
    def __init__(self, speed, color):
        print('the__init__is called')
        print(speed)
        print(color)
        self.speed = speed
        self.color = color

    def test_func():
        print('it passes all functions')

ford = Car(200, 'blue')
honda = Car(300, 'red')
audi = Car(350, 'black')

# ford.speed = 200
# honda.speed = 220
# audi.speed = 250

# ford.color = "red"
# honda.color = "blue"
# audi.color = "black"

# print(ford.speed)
# print(ford.color)

# ford.speed = 300
# ford.color = "blue"