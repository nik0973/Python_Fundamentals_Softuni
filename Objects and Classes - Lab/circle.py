class Circle:
    _pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle._pi * self.diameter

    def calculate_area(self):
        return Circle._pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle._pi * self.radius * self.radius

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
