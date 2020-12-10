# This code is adopted from https://learn.droneblocks.io/p/tello-drone-programming-with-python/


# Tello is a mock of Tello SDK used for communication with drone
class Tello:

    # Send the message to Tello
    def send(self, message):
        self.receive(message)

    # Receive the message from Tello
    def receive(self, msg):
        print("Received message: " + msg)
