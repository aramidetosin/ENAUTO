class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circlCirumference(self):
        return 3.142*2*self.radius
circleA = Circle(8)
print(circleA.radius)
print(circleA.circlCirumference())


circleB = Circle(15)
print(circleB.radius)
print(circleB.circlCirumference())


print(f"The difference between circleA and circleB is {abs(circleA.circlCirumference() - circleB.circlCirumference())}")