## Ashley Speigle
## Lab13_B1
## This gives you the average 
class Grader:

    def __init__(self):
        self.average = 0
        self.total = 0
        self.earned = 0

    def addScore(self, pointsEarned, pointsTotal):
        self.earned += pointsEarned
        self.total += pointsTotal
        self.average += pointsEarned / 3
        

    def getAverage(self):
        return self.average

    def __str__(self):
        print("points earned: ", self.earned)
        print("total points: ", self.total)
        print("the average is: ", self.average)


def main():
    grade = Grader()
    grade.addScore(90,100)
    grade.addScore(56,100)
    grade.addScore(73,100)
    grade.__str__()

main()
