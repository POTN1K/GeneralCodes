import math


class Object(object):
    def __init__(self):
        self.o = (0, 0)
        self.x_coord = 0
        self.y_coord = 0
        self.coord = (self.x_coord, self.y_coord)
        self.distance = 0
        self.coord_list = {self.o}

    def move_vertical(self, new_y):
        self.y_coord = self.y_coord + new_y
        self.coord_list.add((0, new_y))
        self.add_distance(new_y)

    def move_horizontal(self, new_x):
        self.x_coord = self.x_coord + new_x
        self.coord_list.add((new_x, 0))
        self.add_distance(new_x)

    def add_distance(self, new):
        new = abs(new)
        self.distance = self.distance + new

    def get_displacement(self):
        displacement = math.sqrt((math.pow(self.x_coord, 2) + (math.pow(self.y_coord, 2))))
        return displacement


c1 = Object()
c1.move_vertical(3)
c1.move_horizontal(2)
c1.move_horizontal(-5)
c1.move_vertical(-1)
print("Desplazamiento:", c1.get_displacement())
print("Distancia:", c1.distance)

print("\nLa lista es:")
for line in c1.coord_list:
    print(line)

print("\nLa lista es", c1.coord_list)

