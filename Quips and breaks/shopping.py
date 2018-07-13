# Run a scenario whereby the user has to get all of Mrs CCB's shopping items and then she might reveal a little about who she is.
# A list has been created to add the various items to it and then it compares it to the established list.
# For each of the interactions from the menue there is a while lop to keep people in the option until a resolution has been found.
# Once the item has been added to the list then the user exits the loop and can select a new option.
# If the select an option that has already been added the program will let them know that it is no longer a valid option.


def shopping():

    prompt = ">>> "

    grocery_list = []
    grocery_items = ['milk', 'newspaper', 'slippers']

    while grocery_list != grocery_items:
        print("\nItems in your possession: {}".format(grocery_list))
        print("\nYou are standing in the supermaket - What would you like to find?" )
        choice = input(" a) slippers b) newspaper c) milk\n" + prompt)

        if choice == 'a' and 'slippers' not in grocery_list:

            slippers_found = 0

            while slippers_found == 0:
                print("Slippers...where could they be...")
                isle = input("Do you check the a) slippers isle, or b) the freezer section?\n" + prompt)

                if isle == 'a':
                    print("You search high and low, but there are no slippers...")
                    print("Could this have been the work of the malevolent Barbarra?\n")

                elif isle == 'b':
                    print("You check the icecream section...Nope...")
                    print("The vegetable section....Nope...")
                    print("You almost give up hope and then you see them")
                    print("Slippers behind the fish-fingers!!!")
                    print("You thought something smelled fishy - Could this be the work of Barbarra?")
                    print("Slippers added to your cart!\n")
                    slippers_found = 1
                    grocery_list.append('slippers')
                    grocery_list.sort()

                else:
                    print("That isn't a valid option!\n")

        elif choice == 'b' and 'newspaper' not in grocery_list:

            newspaper_choice = 0

            while newspaper_choice == 0:
                print("You walk down the sundries isle and can see ol' lady buscuit Barbarra eying off the last edition of 'The Daily Bake'.")
                print("There is no way you are going to lose to this honeybun.")
                dive = input("Will you dive for the paper (y/n)?\n" + prompt)

                if dive == 'y' or 'Y':
                    print("You have won, Barbarra is down for the count and you have your newspaper\n")
                    grocery_list.append('newspaper')
                    grocery_list.sort()

                elif dive == 'n' or 'N':
                    print("Through some arcane socery you have aquired the paper...Barbarra sensed your intention..."
                          "and backflipped over horseshit to wrangle it from your claws and fell in dramaic fashion, "
                          "leaving you the clear victor. You have your newspaper.\n")
                    newspaper_choice = 1
                    grocery_list.append('newspaper')
                    grocery_list.sort()

                else:
                    print("That isn't a valid option!\n")


        elif choice == 'c'and 'milk' not in grocery_list:

            moo_juice = 0

            while moo_juice == 0:
                print("What milk did Mrs CCB want again...?")
                milk_choice = input("Was is a) full cream b) skim c) apple juice\n" + prompt)

                if milk_choice == 'a':
                    print("Full cream...that doesn't sound right.")
                    print("She's on the all carb no fat diet right now...\n")

                elif milk_choice == 'b':
                    print("Yes, that's right! Enough calcium to keep her sheen, no fat to keep the appeal to the punters alive.\n")
                    moo_juice = 1
                    grocery_list.append('milk')
                    grocery_list.sort()

                elif milk_choice == 'c':
                    print("Wait a second, she was after moo-juie, not apple juice!!\n")

                else:
                    print("That isn't a valid option!\n")



shopping()
print("You have everything required to appease Mrs CCB and perhaps learn an insight or two into what she has been doing...\n")