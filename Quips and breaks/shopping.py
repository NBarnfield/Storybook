# Run a scenario whereby the user has to get all of Mrs CCB's shopping items and then she might reveal a little about who she is.

def shopping():

    grocery_list = []
    grocery_items = ['slippers', 'newspaper', 'milk']

    while grocery_list != grocery_items:
        print("Items in your possession: {}".format(grocery_list))
        print("You are standing in the supermaket - What would you like to find?" )
        choice = input(" a) slippers b) newspaper c) milk")

        if choice == 'a' and grocery_list != 'slippers':
            grocery_list.append('slippers')


        elif choice == 'b' and grocery_list != 'newspaper':
            print("You walk down the sundries isle and can see ol' lady buscuit Barbarra eying off the last edition of 'The Daily Bake.")
            print("There is no way you are going to lose to this honeybun.")
            dive = input("Will you dive for the paper (y/n)? ")
            if dive == 'y' or 'Y':
                print("You have won, Barbarra is down for the count and you have your newspaper")
                grocery_list.append('newspaper')
            else:
                print("Through some arcane socery you have aquired the paper...Barbarra sensed your intention..."
                      "and backflipped over horseshit to wrangle it from your claws and fell in dramaic fashion, "
                      "leaving you the clear victor. You have your newspaper.")
                grocery_list.append('newspaper')

        elif choice == 'c'and grocery_list != 'milk':
            grocery_list.append('milk')
        else:
            print("That isn't a valid option!")
            exit()

shopping()
print("You have everything required to appease Mrs CCB and perhaps learn an insight or two into what she has been doing...")