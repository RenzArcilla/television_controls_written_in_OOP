class TV():  # class
    # parameterized constructor
    def __init__(self, name, channel=0, volume=0):
        self.channel = channel
        self.volume = volume
        self.name = name

    # create method for turning the TV on
    def turn_on(self):
        print(self.name + " is currently on")

    # create method for turning the TV off
    def turn_off(self):
        print(self.name + " is currently off")

    # create method that sets a new channel for the TV object
    def set_new_channel(self):
        while True:
            try:
                self.channel = int(input("Set new channel for " + self.name + ": "))
                break  # Exit the loop if user inputted a valid channel(int)
            except ValueError:
                print("You've submitted an invalid value! Try again.")

    # create method that returns the current channel of the TV object
    def get_current_channel(self):
        return self.channel

    # create method that sets a new volume for the TV object
    def set_new_volume(self):
        while True:
            try:
                self.volume = int(input("Set new volume for " + self.name + ": "))
                break  # Exit the loop if user inputted a valid volume(int)
            except ValueError:
                print("You've submitted an invalid value! Try again.")

    # create method that returns the current volume of the TV object
    def get_current_volume(self):
        return self.volume

    # create method that increases the channel number of the TV object by 1
    def channel_up(self):
        self.channel = self.channel + 1

    # create method that decreases the channel number of the TV object by 1
    def channel_down(self):
        self.channel = self.channel - 1

    # create method that increases the volume of the TV object by 1
    def volume_up(self):
        self.volume = self.volume + 1

    # create method that decreases the volume of the TV object by 1
    def volume_down(self):
        self.volume = self.volume - 1
