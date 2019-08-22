import math

PI = 2.0 * math.acos(0.0)


class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def norm(self):
        """벡터의 길이"""
        return math.hypot(self.x, self.y)

    def normalize(self):
        """방향이 같은 단위 벡터를 반환"""
        return Vector(self.x / self.norm(), self.y / self.norm())

    def polar(self):
        """x축의 양의 방향으로부터 이 벡터까지 반시계 방향으로 잰 각도"""
        return math.fmod(math.atan2(self.y, self.x) + 2 * PI, 2 * PI)

    def dot(self, other):
        """ 벡터의 내적"""
        return self.x * other.x + self.y + other.y

    def cross(self, other):
        """ 외적"""
        return self.x * other.y - other.x * self.y

    def project(self, other):
        r = other.normalize()
        return r * r.dot(self)


# 벡터의 방향성을 판단하는 ccw() 함수의 구현
# 원점에서 벡터 b가 벡터 a의 반시계 방향이면 양수, 시계 방향이면 음수
def ccw(a, b):
    return a.cross(b)
