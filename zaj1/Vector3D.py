import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    @staticmethod
    def are_orthogonal(vector1, vector2):
        return vector1.dot(vector2) == 0

v1 = Vector3D(1,2,3)
v2 = Vector3D(15,20,30)
print(v1)
print(v1.norm())
v1.__setitem__(1,100)
print(v1)
print(v1.__getitem__(0))
print(v1.__add__(v2))
v3 = v1.__add__(v2)
print(v3.__sub__(v1))
print(v3.__mul__(2))
print(v1.dot(v2))
print(v1.cross(v2))
print(Vector3D.are_orthogonal(v1,v3))
v4 = Vector3D(1,0,0)
v5 = Vector3D(0,1,0)
print(Vector3D.are_orthogonal(v4,v5))
