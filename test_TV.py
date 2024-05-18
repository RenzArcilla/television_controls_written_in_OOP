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
#             ask if user wants to turn tv1 on:
#                 call method that turns the television on

#                 ask if the user wants to set a channel for tv1:
#                     call method that asks the user to input a channel

#                 ask if the user wants to increase the channel by 1:
#                     call method that increases the channel by 1:
#                 ask if the user wants to decrease the channel by 1:
#                     call method that decreases the channel by 1:

#                 ask if the user wants to set a volume for tv1
#                     call method that asks the user to input a channel

#                 ask if the user wants to increase the volume by 1:
#                     call method that increases the volume by 1:
#                 ask if the user wants to decrease the volume by 1:
#                     call method that decreases the volume by 1:


#         create an object named tv2
#             ask if user wants to turn tv2 on:
#                 call method that turns the television on

#                 ask if the user wants to set a channel for tv2:
#                     call method that asks the user to input a channel

#                 ask if the user wants to increase the channel by 1:
#                     call method that increases the channel by 1:
#                 ask if the user wants to decrease the channel by 1:
#                     call method that decreases the channel by 1:

#                 ask if the user wants to set a volume for tv1
#                     call method that asks the user to input a channel

#                 ask if the user wants to increase the volume by 1:
#                     call method that increases the volume by 1:
#                 ask if the user wants to decrease the volume by 1:
#                     call method that decreases the volume by 1:
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
