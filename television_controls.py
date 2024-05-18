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

    # create method that sets a new channel for the TV object
    def set_new_channel(self):
        while True:
            try:
                self.channel = int(input("Set new channel for object: "))
                break  # Exit the loop if user inputted a valid int
            except ValueError:
                print("You've submitted an invalid value! Try again.")

    # create method that returns the current channel of the TV object
    def get_current_channel(self):
        return self.channel
