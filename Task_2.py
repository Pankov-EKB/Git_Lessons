class Road:
    def __init__(self, _length, _width):
        self._length_road = _length
        self._width_road = _width

class RoadMass(Road):
    def __init__(self, _length, _width, weight, thickness):
        super().__init__(_length, _width)
        self.weight_road = weight
        self.thickness_road = thickness
    def mass(self):
        return self._length_road * self._width_road * self.weight_road * self.thickness_road

r = RoadMass (25, 10000, 35, 6)
print('Масса асфальта:', r.mass(),'т')