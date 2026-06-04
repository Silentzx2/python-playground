# import random

# class booking:
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked. The Train no is: {self.trainNo}. Form {fro} to {to} ")

#     def getstatus(self):
#         print(f"Train no: {self.trainNo} is running on time")

#     def getfare(self, fro, to):
#         print(f"Ticket fare in Train no: {self.trainNo}. Form {fro} to {to} is: {random.randint(243,3453)}")

# t = booking(4353)
# t.book("asansol", "puri")
# t.getstatus()
# t.getfare("asansol", "puri")

import random
class train:
    def __init__(self, TrainNo, fro, to):
        self.TrainNo = TrainNo
        self.fro = fro
        self.to = to
        seat_type = ["upper", "lower", "middle"]
        print("Welcome to Indian Railway")
        print(f"Ticket is booked. Train no is: {TrainNo} Seat no: {random.randint(1, 100)}, {random.choice(seat_type)} form {fro} To {to} ")

    def getstatus(self):
        print(f"The train no: {self.TrainNo} is running on time")

T = train(4532, "asansol", "puri")
T.getstatus()