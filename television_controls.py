class TV():  # class
    # parameterized constructor
    def __init__(self, channel, volume, on_or_off):
        self.channel = channel
        self.volume = volume
        self.on_or_off = on_or_off

    # create method for turning the TV on
    def turn_on(self):
        print("object " + "is currently on")

    # create method for turning the TV off
    def turn_off(self):
        print("object " + "is currently off")
