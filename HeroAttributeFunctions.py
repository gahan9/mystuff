# constants
ATTRIBUTES = {"STRENGTH": 0, "DEXTERITY": 0, "WISDOM": 0, "HEALTH": 0}
TOTAL_POINTS = 30
userInput = None


def create_character():
    """

    :return: name : of character
    """
    name = str(input("\nCharacter Name: "))
    ATTRIBUTES['character'] = name
    print("\nYour character's name is now: " + name)
    input("\nPress 'Enter' to return to menu.")
    return name  # returns name entered by user which can be stored and retrive in other function


def change_attributes(char_name="", flag="add"):
    """

    :param char_name: name of character
    :param flag: add/sub to make sure which function to call to change attributes value
    :return: this either returns true or false or none
    """
    global TOTAL_POINTS
    name = char_name
    if 'character' in ATTRIBUTES.keys():  # user needs to create character first before assigning any attributes
        # What attribute?
        print(name + "'s Attribute Stats are:\n")
        for attrName in ATTRIBUTES:
            print(attrName, ":\t", str(ATTRIBUTES[attrName]))
        print("UNUSED POINTS:" + "\t" + str(TOTAL_POINTS))
        changeAttr = input("What attribute would you like to change? ").upper()

        if flag == "add":
            result = add_points(changeAttr, name)
        elif flag == "sub":
            result = remove_points(changeAttr, name)
        if result:
            return True
        else:
            print("That is an invalid choice.")
            choice = input("Do you want to try again ?... (Y/N)").upper()
            if choice == "Y":
                change_attributes(name, flag)
            elif choice == "N":
                print("Have a nice day!!!")
                return False
            else:
                print("Invalid input.")
                return False
    else:
        print('You need to create character first.')


def add_points(changeAttr, char_name):
    """
    add points to attribute
    :param changeAttr: attributes which is to be change
    :param char_name: character name whose attribute value to be change
    :return: True/False
    """
    global TOTAL_POINTS  # it is good habit to specify global keyword to know function it is not local variable otherwise you may get UnboundLocalError
    global ATTRIBUTES
    name = char_name
    if changeAttr in ATTRIBUTES:
        try:
            changePoints = abs(int(input(
                "How many points would you like to add? ")))  # converts negative input to positive or use another control statement to handle value input.
        except ValueError:
            print("Invalid values. Please enter integer value only")

        if 0 < changePoints < TOTAL_POINTS:  # make sure points to insert is greater than 0 and less than total points
            ATTRIBUTES[changeAttr] += changePoints
            TOTAL_POINTS -= changePoints
            print("\n" + name + "'s Attribute Stats are now:\n")
            for attrName in ATTRIBUTES:
                print(attrName, ":\t", str(ATTRIBUTES[attrName]))
            print("UNUSED POINTS:" + "\t " + str(TOTAL_POINTS))
            return True
        else:
            print("You can only add minimum {} points and maximum {} points".format(1, TOTAL_POINTS))
            choice = input("Do you want to try again ?... (Y/N)").upper()
            if choice == "Y":
                change_attributes(name, "add")
            elif choice == "N":
                print("Have a nice day!!!")
                return False
            else:
                print("Invalid input.")
                return False
    else:
        return False


def remove_points(changeAttr, char_name):
    """
    remove points of attribute
    :param changeAttr: attributes which is to be change
    :param char_name: character name whose attribute value to be change
    :return: True/False
    """
    global TOTAL_POINTS
    global ATTRIBUTES
    name = char_name
    if changeAttr in ATTRIBUTES:
        if ATTRIBUTES[changeAttr] > 0:  # only remove attributes if it has value
            changePoints = abs(int(input("How many points would you like to remove? ")))
            if 0 < changePoints < ATTRIBUTES[changeAttr]:
                ATTRIBUTES[changeAttr] -= changePoints
                TOTAL_POINTS += changePoints
                print("\n" + name + "'s Attribute Stats are now:\n")
                for attrName in ATTRIBUTES:
                    print(attrName, ":\t", str(ATTRIBUTES[attrName]))
                print("UNUSED POINTS:" + "\t " + str(TOTAL_POINTS))
                return True
            else:
                print("You can only remove minimum {} points and maximum {} points".format(1, ATTRIBUTES[changeAttr]))
                # give a chance to input again with function call
                choice = input("Do you want to try again ?... (Y/N)").upper()
                if choice == "Y":
                    change_attributes(name,
                                      "sub")  # you can also call same function remove_points() with valid arguments if you want user to enter only selected field again
                elif choice == "N":
                    print("Have a nice day!!!")
                    return False
                else:
                    print("Invalid input.")
                    return False
        else:
            print("no attributes left to remove.")
            sel = input("Do you want to add points first ?... (Y/N)").upper()
            if sel == "Y":
                change_attributes(name, "add")
            elif sel == "N":
                print("Have a nice day!!!")
                return False
            else:
                print("Invalid input.")
                return False
    else:
        return False


if __name__ == "__main__":
    while userInput != "5":
        userInput = input \
            ("""
    Character Creator

    1 - Name Character
    2 - Assign Attribute Points
    3 - Remove Attribute Points
    4 - Exit

    >> """)
        # Name Character
        if userInput == "1":
            character_name = create_character()

        # Assign Points
        elif userInput == "2":
            try:
                change_attributes(character_name, "add")
            except NameError:
                print("You need to create character first!!!!!")
                choice1 = input("want to try again? (Y/N)").upper()
                if choice1 == "Y":
                    pass
                else:
                    break
        # Remove Points
        elif userInput == "3":
            try:
                change_attributes(character_name, "sub")
            except NameError:
                print("You need a character with valid attributes...")
                choice2 = input("want to try again? (Y/N)").upper()
                if choice2 == "Y":
                    pass
                else:
                    break
        # Exit  
        elif userInput == "4":
            break

        # Invalid Choice in Menu
        else:
            print("\nInvalid choice...")

    input("Press 'Enter' to exit.")
