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

valid_inputs = ("yes", "no")  # will be used for catching errors

tv1 = TV("tv1")  # create an object named tv1

off_or_on = "this_is_a_wrong_input"
while off_or_on not in valid_inputs:
    off_or_on = input("Would you like to turn tv1 on (yes/no)? ")
    if off_or_on == "no":
        tv1.turn_off()
        break

    if off_or_on == "yes":
        while True:
            tv1.turn_on()
            print("")

            user_channel = "this_is_a_wrong_input"
            while user_channel not in valid_inputs:
                user_channel = input("Would you like to input a new channel (yes/no)? ")
                if user_channel == "yes":
                    tv1.set_new_channel()
                    print("")
                    break
                elif user_channel == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_channel_up = "this_is_a_wrong_input"
            while user_channel_up not in valid_inputs:
                user_channel_up = input("Would you like to increase channel by 1 (yes/no)? ")
                if user_channel_up == "yes":
                    tv1.channel_up()
                    print("")
                    break
                elif user_channel_up == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_channel_down = "this_is_a_wrong_input"
            while user_channel_down not in valid_inputs:
                user_channel_down = input("Would you like to decrease channel by 1 (yes/no)? ")
                if user_channel_down == "yes":
                    tv1.channel_down()
                    print("")
                    break
                elif user_channel_down == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_volume = "this_is_a_wrong_input"
            while user_volume not in valid_inputs:
                user_volume = input("Would you like to input a new volume (yes/no)? ")
                if user_volume == "yes":
                    tv1.set_new_volume()
                    print("")
                    break
                elif user_volume == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_volume_up = "this_is_a_wrong_input"
            while user_volume_up not in valid_inputs:
                user_volume_up = input("Would you like to increase volume by 1 (yes/no)? ")
                if user_volume_up == "yes":
                    tv1.volume_up()
                    print("")
                    break
                elif user_volume_up == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_volume_down = "this_is_a_wrong_input"
            while user_volume_down not in valid_inputs:
                user_volume_down = input("Would you like to decrease volume by 1 (yes/no)? ")
                if user_volume_down == "yes":
                    tv1.volume_down()
                    print("")
                    break
                elif user_volume_down == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_get_channel = "this_is_a_wrong_input"
            while user_get_channel not in valid_inputs:
                user_get_channel = input("Would you like to know the current channel (yes/no)? ")
                if user_get_channel == "yes":
                    current_channel = tv1.get_current_channel()
                    print("The current channel is: " + str(current_channel))
                    print("")
                    break
                elif user_get_channel == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_get_volume = "this_is_a_wrong_input"
            while user_get_volume not in valid_inputs:
                user_get_volume = input("Would you like to know the current volume (yes/no)? ")
                if user_get_volume == "yes":
                    current_volume = tv1.get_current_volume()
                    print("The current channel is: " + str(current_volume))
                    print("")
                    break
                elif user_get_volume == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_turn_off = "this_is_a_wrong_input"
            while user_turn_off not in valid_inputs:
                user_turn_off = input("Would you like to turn tv1 off (yes/no)? ")
                if user_turn_off in valid_inputs:
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            if user_turn_off == "no":
                continue
            elif user_turn_off == "yes":
                tv1.turn_off()
                break

    else:
        print("You've inputted an invalid value. Choose again")


tv2 = TV("tv2")  # creates an object named tv2

off_or_on = "this_is_a_wrong_input"
while off_or_on not in valid_inputs:
    off_or_on = input("Would you like to turn tv2 on (yes/no)? ")
    if off_or_on == "no":
        tv2.turn_off()
        break

    if off_or_on == "yes":
        while True:
            tv2.turn_on()
            print("")

            user_channel = "this_is_a_wrong_input"
            while user_channel not in valid_inputs:
                user_channel = input("Would you like to input a new channel (yes/no)? ")
                if user_channel == "yes":
                    tv2.set_new_channel()
                    print("")
                    break
                elif user_channel == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_channel_up = "this_is_a_wrong_input"
            while user_channel_up not in valid_inputs:
                user_channel_up = input("Would you like to increase channel by 1 (yes/no)? ")
                if user_channel_up == "yes":
                    tv2.channel_up()
                    print("")
                    break
                elif user_channel_up == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_channel_down = "this_is_a_wrong_input"
            while user_channel_down not in valid_inputs:
                user_channel_down = input("Would you like to decrease channel by 1 (yes/no)? ")
                if user_channel_down == "yes":
                    tv2.channel_down()
                    print("")
                    break
                elif user_channel_down == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_volume = "this_is_a_wrong_input"
            while user_volume not in valid_inputs:
                user_volume = input("Would you like to input a new volume (yes/no)? ")
                if user_volume == "yes":
                    tv2.set_new_volume()
                    print("")
                    break
                elif user_volume == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_volume_up = "this_is_a_wrong_input"
            while user_volume_up not in valid_inputs:
                user_volume_up = input("Would you like to increase volume by 1 (yes/no)? ")
                if user_volume_up == "yes":
                    tv2.volume_up()
                    print("")
                    break
                elif user_volume_up == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_volume_down = "this_is_a_wrong_input"
            while user_volume_down not in valid_inputs:
                user_volume_down = input("Would you like to decrease volume by 1 (yes/no)? ")
                if user_volume_down == "yes":
                    tv2.volume_down()
                    print("")
                    break
                elif user_volume_down == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_get_channel = "this_is_a_wrong_input"
            while user_get_channel not in valid_inputs:
                user_get_channel = input("Would you like to know the current channel (yes/no)? ")
                if user_get_channel == "yes":
                    current_channel = tv2.get_current_channel()
                    print("The current channel is: " + str(current_channel))
                    print("")
                    break
                elif user_get_channel == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_get_volume = "this_is_a_wrong_input"
            while user_get_volume not in valid_inputs:
                user_get_volume = input("Would you like to know the current volume (yes/no)? ")
                if user_get_volume == "yes":
                    current_volume = tv2.get_current_volume()
                    print("The current channel is: " + str(current_volume))
                    print("")
                    break
                elif user_get_volume == "no":
                    print("")
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            user_turn_off = "this_is_a_wrong_input"
            while user_turn_off not in valid_inputs:
                user_turn_off = input("Would you like to turn tv1 off (yes/no)? ")
                if user_turn_off in valid_inputs:
                    break
                else:
                    print("You've inputted an invalid value. Choose again")

            if user_turn_off == "no":
                continue
            elif user_turn_off == "yes":
                tv2.turn_off()
                break

    else:
        print("You've inputted an invalid value. Choose again")
