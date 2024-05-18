# pseudocode:
#     start:
#         create a class named TV
#             create constructor
#                 create parameters for channel, volume, and on_or_off

#             create method for turning the TV on
#             create method for turning the TV off

#             create method that sets a new channel for the TV object
#             create method that returns the current channel of the TV object

#             create method that sets a new volume for the TV object
#             create method that returns the current volume of the TV object

#             create method that increases the channel number of the TV object by 1
#             create method that decreases the channel number of the TV object by 1

#             create method that increases the volume of the TV object by 1
#             create method that decreases the volume of the TV object by 1
#
#         create an object named tv1
#             turn tv1 on
#             set channel of tv1 to 30
#             increase channel of tv1 by 1
#             decrease channel of tv1 by 1
#             set volume of tv1 to 3
#             increase volume of tv1 by 1
#             decrease volume of tv1 by 1
#             get the current channel and volume of tv1

#         create an object named tv2
#             turn tv2 on
#             set channel of tv2 to 3
#             increase channel of tv2 by 1
#             decrease channel of tv2 by 1
#             set volume of tv2 to 2
#             increase volume of tv2 by 1
#             decrease volume of tv2 by 1
#             get the current channel and volume of tv2
#     end:

from television_controls import TV

tv1 = TV("tv1")  # creates an object
tv1.turn_on()  # calls a method
tv1.set_new_channel()
tv1.channel_up()
tv1.channel_down()
tv1.set_new_volume()
tv1.volume_up()
tv1.volume_down()
tv1.get_current_channel()
tv1.get_current_volume()
tv1.turn_off()

tv2 = TV("tv2")  # creates an object
tv2.turn_on()  # calls a method
tv2.set_new_channel()
tv2.channel_up()
tv2.channel_down()
tv2.set_new_volume()
tv2.volume_up()
tv2.volume_down()
tv2.get_current_channel()
tv2.get_current_volume()
tv2.turn_off()
