# __author__  = Wilsen Maitre
# The program will welcome the user and from their choice run a specific code.
# Either a space or math related task.
# Horoscopes for your Sun and Rising Signs : later(Final Sprint) : Files
def main():
    import random  # Pre built function. Generate random number.
    continue_program = True
    while continue_program:  # This will make the program run until the user
        # tells it to stop.
        print("\nWelcome to Project Apollo!")
        print("1. Motivational quotes")
        print("2. Astrological sign")
        print("3. Exploring the Sun and the Moon")
        print("4. The Guessing Game. You have three attempts")
        print("5. Calculate the Distance between two points")
        print("6. Calculate the Midpoint of a line")
        print("7. Calculate Dot Product")
        print("8. The Ladder Game")
        print("9. Random Stuff")
        print("10. Quit")
        user_choice = int(input("To begin choose from one of the following: "))
        while user_choice < 1 or user_choice > 10:  # This will make sure the
            # user input a correct number and if not will prompt him/her to
            # make the correct choice.
            print("Please input a correct number between 1 and 10")
            user_choice = int(input("Answer: "))
        if user_choice == 1:
            user_name = input("What is your name: ")
            user_num = int(input("Pick a number between 1 and 10: "))
            while user_choice < 1 or user_choice > 10:
                print("Please input a correct number between 1 and 10")
                user_choice = int(input("Answer: "))
            if 0 < user_num < 11: #simplified way. Other way can be done
                # with (and) operator.
                print("Hello ", user_name, "you have a goal in mind Use your "
                                           "ambition, drive and desire—along "
                                           "with these 2 motivational "
                                           "quotes—to make it happen.")
                power_move()
        elif user_choice == 2:
            astrological() # This is a call and it will go to the function
            # (def) and run the programs.
        elif user_choice == 3:
            solar_system()
        elif user_choice == 4:
            for random_number in range(3):  # 1,2,3
                user_num = int(input("\nEnter a number between 1 and 10: "))
                while user_num > 10 or user_num < 1:
                    user_num = int(input("Invalid number. Enter a number "
                                         "between 1 and 10: "))
                rand_num = random.randint(1, 10)  # get a random number.
                print("Computer number:", rand_num)
                print("User number:", user_num)
                print(random_computer_n(user_num, rand_num))  # function
                # parameter
        elif user_choice == 5:
            import math  # w3 schools for import the sqrt function
            print("\nCalculating the distance of two points.")
            x1 = int(input("Coordinates of the first point (x1): "))
            x2 = int(input("Coordinates of the first point (x2): "))
            y1 = int(input("Coordinates of the second point (y1): "))
            y2 = int(input("Coordinates of the second point (y2): "))
            x_distance = (x2 - x1) ** 2 # ** exponent.Will raise the value
            # by 2.
            y_distance = (y2 - y1) ** 2  # - will subtract the two values
            distance = math.sqrt(x_distance + y_distance)
            print("The distance is: ", format(distance, '.2f')) #2 sig fig
        elif user_choice == 6:
            print("Calculating the midpoint of a line.")
            x1 = int(input("The value of x1 (the first endpoint): "))
            y1 = int(input("The value of y1 (the first endpoint): "))
            x2 = int(input("The value of x2 (the second endpoint): "))
            y2 = int(input("The value of y2 (the second endpoint): "))
            x_midpoint = (x1 + x2) / 2  # + will add the two integer
            y_midpoint = (y1 + y2) // 2  # / will divide the value by 2
            print("The midpoint of line is:",
                  format(x_midpoint, '.2f') + "," + format(y_midpoint, '.2f'))
        elif user_choice == 7:
            print("Calculating the Dot Product.")
            u1 = int(input("Enter the value for u1: "))
            u2 = int(input("Enter the value for u2: "))
            v1 = int(input("Enter the value for v1: "))
            v2 = int(input("Enter the value for v2: "))
            print("The dot product is: ", (u1 * v1) + (u2 * v2))
        elif user_choice == 8:
            print("Welcome to the Ladder Game")
            start_up = int(input("Enter a number between 1 and 9: "))
            while start_up < 1 or start_up > 9:
                print("Please input a correct number between 1 and 9")
                start_up = int(input("Answer: "))
            for row in range(1, start_up + 1):
                for collumn in range(1, row + 1):
                    print(collumn, end=" ")
                print()
        elif user_choice == 9:
            triangle = int(input("Pick a number between 1 and 10: "))
            name = input("What is your name: ")
            while user_choice < 1 or user_choice > 10:
                print("Please input a correct number between 1 and 10")
                user_choice = int(input("Answer: "))
            print(name + " Thank you for playing, here's a triangle.")
            for built in range(1, triangle + 1):
                print("* " * built)
            print("\nHere take these even numbers too.")
            x = 1
            while x <= 10:
                if x % 2 == 0:
                    print(x, end=" ")
                x += 1
            print("\n")
        else:
            print("Thank You.")
            continue_program = False

def astrological():
    global astro_sign
    user_name = input("What is your first name: ")
    birthday = int(input("What is your birthday, enter a number: "))
    while birthday < 1 or birthday > 31:  # This will make sure the
        # user input a correct number and if not will prompt him/her to
        # make the correct choice.
        print("Please input a correct number")
        birthday = int(input("What is your birthday, i.e. a number: "))
    birthmonth = int(input("What is your birthmonth, i.e. a number: "))
    while birthmonth < 1 or birthmonth > 12:
        print("Please input a correct number")
        birthmonth = int(input("What is your birthmonth, i.e. a number: "))
    if birthmonth == 1:  # One line if statement in Python. Pythoncentral.io
        astro_sign = "Capricorn" if (birthday < 20) else "Aquarius"
    elif birthmonth == 2:
        astro_sign = "Aquarius" if (birthday < 19) else "Pisces"
    elif birthmonth == 3:
        astro_sign = "Pisces" if (birthday < 21) else "Aries"
    elif birthmonth == 4:
        astro_sign = "Aries" if (birthday < 20) else "Taurus"
    elif birthmonth == 5:
        astro_sign = "Taurus" if (birthday < 21) else "Gemini"
    elif birthmonth == 6:
        astro_sign = "Gemini" if (birthday < 21) else "Cancer"
    elif birthmonth == 7:
        astro_sign = "Cancer" if (birthday < 23) else "Leo"
    elif birthmonth == 8:
        astro_sign = "Leo" if (birthday < 23) else "Virgo"
    elif birthmonth == 9:
        astro_sign = "Virgo" if (birthday < 23) else "Libra"
    elif birthmonth == 10:
        astro_sign = "Libra" if (birthday < 23) else 'scorpio'
    elif birthmonth == 11:
        astro_sign = "Scorpio" if (birthday < 22) else "Sagittarius"
    elif birthmonth == 12:
        astro_sign = "Sagittarius" if (birthday < 22) else "Capricorn"
    else:
        print("Invalid input")
    print(user_name, "Your Astrological sign is:", astro_sign, sep=" ")
    #PEP8 error astro_sign: Local variable 'astro_sign' might be referenced
    # before assignment. Needs to be Global.
    print("Would you like to know your elemental sign? Y/N")
    element_sign = (input("Continue Y/N: "))
    big_letter = element_sign.capitalize()  # Capitalize your answer# w3schools
    continue_program = True
    while continue_program:
        if big_letter == "Y":
            if birthmonth == 6 or birthmonth == 10 or birthmonth == 2:
                element_air()
                print("\n")
                break  # To exit the loop
            elif birthmonth == 5 or birthmonth == 9 or birthmonth == 1:
                element_earth()
                print("\n")
                break
            elif birthmonth == 4 or birthmonth == 8 or birthmonth == 12:
                element_fire()
                print("\n")
                break
            elif birthmonth == 7 or birthmonth == 11 or birthmonth == 3:
                element_water()
                print("\n")
                break
        elif big_letter == "N":
            print("Thank You. How about you choose another task.")
            break
        else:
            print("Choose a correct letter, Y or N")
            element_sign = (input("Continue Y/N: "))
            big_letter = element_sign.capitalize()

def element_air():
    print("The Air Signs are: Gemini, Libra and Aquarius.\nAir signs are "
          "rational, social, and love communication and relationships with "
          "other people.\nThey are thinkers, friendly, intellectual, "
          "communicative and analytical. \nBut just as wind can be a light "
          "breeze or a destructive tornado, these signs also know how to "
          "pack a punch! \nWithout air,we struggle to apply logic where "
          "needed and to keep our cool in tough situations. ")

def element_fire():
    print("The Fire Signs are: Aries, Leo and Sagittarius.\nFire signs tend to"
          "be passionate, dynamic, and temperamental. They get angry quickly, "
          "but they also forgive easily. \nThey are adventurers with immense "
          "energy. They are physically very strong and are a source of"
          "inspiration for others.\nFire signs are intelligent, self-aware, "
          "creative and idealistic people, always ready for action."
          "\nUnregulated fire energy can scorch others-inherently, "
          "fire doesn't take into account the cause and effect of its "
          "actions.\nBut without fire, its difficult to find motivation. ")

def element_earth():
    print("The Earth Signs are: Taurus, Virgo and Capricorn.\nEarth signs are "
          "'grounded' and the ones that bring us down to earth.\nThey are "
          "mostly conservative and realistic, but they can also be very "
          "emotional. \nThey are practical, loyal and stable and they stick "
          "by their people through hard times.\nToo much earth energy can be "
          "over-indulgent, materialistic and lacking innovation.\nToo little "
          "earth energy, on the other hand, can make it challenging to turn "
          "ideas into reality.")

def element_water():
    print("The Water Signs are: Cancer, Scorpio and Pisces.\nWater signs are "
          "exceptionally emotional and ultra-sensitive. They are highly "
          "intuitive and they can be as mysterious as the ocean itself. "
          "\nWater signs love profound conversations and intimacy. They rarely"
          "do anything openly and are always there to support their loved "
          "ones.\nExcessive water creates a flood of escapism, confusion and "
          "hyper-sensitivity. ")

def solar_system():
    print("\nLets start learning about the two galactic bodies in our solar "
          "system. The Sun and the Moon.")
    system_choice = int((input("Continue, 1 for yes, 0 for no: ")))
    while not (system_choice == 1 or system_choice == 0):  # The return value
        # will be True if the statement(s) are not True, otherwise it will
        # return False. Reverses the boolean statement
        print("Please input a correct number. 1 = yes, 0 = no:")
        system_choice = int((input("Continue, 1 for yes, 0 for no: ")))

    if system_choice == 1:
        print("Your sun sign (determined by the position of the sun at the "
              "time of your birth) is a key astrological entry point. It "
              "shows your personality, preferences, and attitude. \nThe Sun is"
              "associated with Leo. Both the celestial body and the fiery "
              "zodiac sign love to be the center of attention. \nThe Sun also "
              "exposes your unique hero's journey the triumphs and trials "
              "experienced in your lifetime. \nWithin the natal chart, the Sun"
              "represents your ego, sense of self, and fundamental essence."
              "\nNext topic: MOON \n")

        system_choice = int((input("Continue, 1 for yes, 0 for no: ")))
        while not (system_choice == 1 or system_choice == 0):
            print("Please input a correct number. 1 = yes, 0 = no:")
            system_choice = int((input("Continue, 1 for yes, 0 for no: ")))
        if system_choice == 1:
            print("\nThe Moon is considered an inner-planet and takes "
                  "approximately 2.5 days to transit a sign. \nThe Moon rules "
                  "the zodiac sign of Cancer and dictates a big part of your "
                  "daily astrology. \nThe sign that the Moon occupies will "
                  "tell you about the collective mood of the day and how people"
                  "are approaching current affairs. \nLunar phases can also "
                  "tell us if we should be planning ahead or reviewing the past."
                  "\nThe Moon symbolizes the concept of the mother, and its "
                  "placement in your birth chart represents how you mother "
                  "yourself through both material and non material comforts."
                  "\nThank You. How about you choose another category.\n")
        else:
            print("\nThank You. How about you choose another category\n")
    else:
        print("\nThank You. How about you choose another category\n")

def random_computer_n(your_num, computer_num):
    if not your_num != computer_num:  # Reverse the result
        return "You picked the same number as the computer!" #end the
        # program and return the answer
    if your_num < computer_num:
        return "Your number is smaller than the computer's number."
    if your_num > computer_num:
        return "Your number is higher than the computer's number."

def power_move():
    print(
        "\nI’ve missed more than 9,000 shots in my career. I’ve lost almost "
        "300 games. 26 times I’ve been trusted to take the game winning shot "
        "and missed. \nI’ve failed over and over and over again in my life "
        "and that is why I succeed.” – Michael Jordan\n\nWe need to accept "
        "that we won’t always make the right decisions, that we’ll screw up "
        "royally sometimes – understanding that failure is not the opposite "
        "of success, \nit’s part of success. – Arianna Huffington")

main()
