from random import randint
class train():
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(harry, fro, to):
        print(f"Dear customer your ticked is booked you train no is: {harry.trainNo} from station {fro} to {to}")

    def getstatus(self):
        print(f"Dear customer your {self.trainNo} is on time")

    def getfare(self, fro, to):
        print(f"Dear customer ticket fare in train no: {self.trainNo} from station {fro} to {to} is {randint(2423, 76856)}")

t = train(3534)
t.book("rampur", "asansol")
t.getstatus()
t.getfare("rampur", "asansol")