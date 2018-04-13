class performer:

    def __init__(self):
        self.position = 0
        self.ropeleng = 10

    def forward(self):
        if self.position < self.ropeleng:
            self.position += 1

    def backward(self):
        if self.position > 0:
            self.position -= 1

    def getPosition(self):
        return self.position


p1 = performer()

print("Initial position:", p1.getPosition())

p1.forward()
p1.forward()
p1.forward()
p1.forward()

print("After moving forward the position is:",p1.getPosition())

p1.backward()
print("After moving backward:", p1.getPosition())
