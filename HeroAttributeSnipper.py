# Hero Attribute Assigner
# My attempt

name = ""
attr = {"STRENGTH":0, "DEXTERITY":0, "WISDOM":0, "HEALTH":0}
totalPoints = 30
userInput = None
while userInput != "5":
    userInput = input \
    ("""
Character Creator

1 - Name Character
2 - Assign Attribute Points
3 - Remove Attribute Points
4 - Exit

:    """)
    # Name Character
    if userInput == "1":
        name = str(input("\nCharacter Name: "))
        attr['character'] = name
        print("\nYour character's name is now: " + name)
        input("\nPress 'Enter' to return to menu.")

    # Assign Points
    elif userInput == "2":
        if 'character' in attr.keys(): # user needs to create character first before assigning any attributes
            # What attribute?
            print("\n" + name + "'s Attribute Stats are:\n")
            for attrName in attr:
                print(attrName, ":\t", str(attr[attrName]))
            print("UNUSED POINTS:" + "\t" + str(totalPoints))
            changeAttr = input("\nWhat attribute would you like to add points to? ").upper()
            # How many points to add?
            if changeAttr in attr:
                try:
                    changePoints = abs(int(input("How many points would you like to add? "))) # converts negative input to positive or use another control statement to handle value input.
                except ValueError:
                    print("Invalid values. Please enter integer value only")
                if  0 < changePoints < totalPoints: # make sure points to insert is greater than 0 and less than total points
                    attr[changeAttr] += changePoints
                    totalPoints -= changePoints
                    print("\n" + name + "'s Attribute Stats are now:\n")
                    for attrName in attr:
                        print(attrName, ":\t", str(attr[attrName]))
                    print("UNUSED POINTS:" + "\t " + str(totalPoints))
                else:
                    print("You can only add minimum {} points and maximum {} points".format(1, totalPoints))
            else:
                print("\nThat is not a valid choice.")
        else:
            print('You need to create character first.')

    # Remove Points
    elif userInput == "3":
        if 'character' in attr.keys():
            # What attribute?
            print("\n" + name + "'s Attribute Stats are:\n")
            for attrName in attr:
                print(attrName, ":\t", str(attr[attrName]))
            print("UNUSED POINTS:" + "\t" + str(totalPoints))
            changeAttr = input("\nWhat attribute would you like to remove points from? ").upper()

            # How many points to remove?
            if changeAttr in attr:
                if attr[changeAttr] > 0: # only remove attributes if it has value
                    changePoints = abs(int(input("How many points would you like to remove? ")))
                    if 0 < changePoints < attr[changeAttr]:
                        attr[changeAttr] -= changePoints
                        totalPoints += changePoints
                        print("\n" + name + "'s Attribute Stats are now:\n")
                        for attrName in attr:
                            print(attrName, ":\t", str(attr[attrName]))
                        print("UNUSED POINTS:" + "\t " + str(totalPoints))
                    else:
                        print("You can only remove minimum {} points and maximum {} points".format(1, attr[changeAttr]))
                else:
                    print("no attributes left to remove.")
            else:
                print("\nThat is not a valid amount.")
        else:
            print('You need to create character first.')

    # Exit  
    elif userInput == "4":
        break

    # Invalid Choice in Menu
    else:
        print("\nInvalid choice...")

input("\nPress 'Enter' to exit.")
