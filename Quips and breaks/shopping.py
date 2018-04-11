# Run a scenario whereby the user has to get all of Mrs CCB's shopping items and then she might reveal a little about who she is.

def shopping():

    grocery_list = []
    grocery_items = ['milk', 'newspaper', 'slippers']

    while grocery_list != grocery_items:
        print("\nItems in your possession: {}".format(grocery_list))
        print("\nYou are standing in the supermaket - What would you like to find?" )
        choice = input(" a) slippers b) newspaper c) milk")

        if choice == 'a' and 'slippers' not in grocery_list:
            print("")
            grocery_list.append('slippers')
            grocery_list.sort()

        elif choice == 'b' and 'newspaper' not in grocery_list:
            print("You walk down the sundries isle and can see ol' lady buscuit Barbarra eying off the last edition of 'The Daily Bake'.")
            print("There is no way you are going to lose to this honeybun.")
            dive = input("Will you dive for the paper (y/n)? ")
            if dive == 'y' or 'Y':
                print("You have won, Barbarra is down for the count and you have your newspaper")
                grocery_list.append('newspaper')
                grocery_list.sort()

            else:
                print("Through some arcane socery you have aquired the paper...Barbarra sensed your intention..."
                      "and backflipped over horseshit to wrangle it from your claws and fell in dramaic fashion, "
                      "leaving you the clear victor. You have your newspaper.")
                grocery_list.append('newspaper')
                grocery_list.sort()

        elif choice == 'c'and 'milk' not in grocery_list:
            grocery_list.append('milk')
            grocery_list.sort()

        else:
            print("That isn't a valid option!")

shopping()
print("You have everything required to appease Mrs CCB and perhaps learn an insight or two into what she has been doing...")