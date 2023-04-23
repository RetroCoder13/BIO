class Rotor:
    def __init__(self, portLeft, portRight):
        self.portLeft = portLeft
        self.portRight = portRight
        self.rotations = 0

    def leftToRight(self, input):
        output = self.portRight[self.portLeft.index(input)]
        return output
    def rightToLeft(self, input):
        output = self.portLeft[self.portRight.index(input)]
        return output
    def rotate(self):
        for index,item in enumerate(self.portLeft):
            if item == "A":
                self.portLeft[index] = "D"
            if item == "B":
                self.portLeft[index] = "A"
            if item == "C":
                self.portLeft[index] = "B"
            if item == "D":
                self.portLeft[index] = "C"
        for index,item in enumerate(self.portRight):
            if item == "A":
                self.portRight[index] = "D"
            if item == "B":
                self.portRight[index] = "A"
            if item == "C":
                self.portRight[index] = "B"
            if item == "D":
                self.portRight[index] = "C"

        self.rotations += 1

startingRotation = int(input())
string = input().upper()
finalString = ""

rotor1 = Rotor(["A","B","C","D"],["A","D","B","C"])
rotor2 = Rotor(["A","B","C","D"],["A","C","B","D"])
reflector = Rotor(["A","B","C","D"], ["D","C","B","A"])

for i in range(startingRotation):
    rotor1.rotate()
    if rotor1.rotations % 4 == 0:
        rotor2.rotate()

for index,item in enumerate(string):
    finalString += rotor1.rightToLeft(rotor2.rightToLeft(reflector.leftToRight(rotor2.leftToRight(rotor1.leftToRight(item)))))
    rotor1.rotate()
    if rotor1.rotations % 4 == 0:
        rotor2.rotate()

print(finalString)

# print(rotor1.rightToLeft(rotor2.rightToLeft(reflector.leftToRight(rotor2.leftToRight(rotor1.leftToRight("D"))))))