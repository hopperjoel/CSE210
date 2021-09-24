class Rectangle:
    def __init__(self):
        pass

    def stuff(self, engine):
        self.engine = engine

car_a = Rectangle()
car_b = Rectangle()

car_b.stuff('v8')

print(car_b.engine)

# shape_1.width = 100
# shape_2.width = 150
# shape_3.width = 200

# shape_1.height  = 200
# shape_2.height = 300
# shape_3.height = 400

# shape_1.area = shape_1.width * shape_1.height

# print(shape_1.area)