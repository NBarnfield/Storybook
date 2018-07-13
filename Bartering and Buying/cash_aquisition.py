# Run a scenario whereby the user has to get cash for future transactions by looking various places.
# A counter

def cash_aquisition():

    prompt = ">>> "

    cash = 0

    while cash < 3:

        print("Current Cash: {}".format(cash))
        print("\nYou need to find enough cash to purchase all of the things that Mrs CCB has put on the shopping list.")
        print("\nYou don't currently have your debit card on you, so you will have to source your funds elsewhere.")
        print("\nwhere will you start looking?")
        choice = input("a) behind the couch b) in the fridge c) in the pantry\n" + prompt)

        if choice == 'a':

            couch_money = 0

            while couch_money == 0:
                print("You snoop around the front, the sides and finally you look BEHIND the couch...")
                cushion = input("There are 2 cushions...Do you check the a) left cushion, or b) right cushion?\n" + prompt)

                if cushion == 'a':
                    print("You lift the left cushion...")
                    print("Bob the snail is sleeping beneath it! You put the cushion back - a cranky Bob is not worth a dollar!!\n")

                elif cushion == 'b':
                    print("In lifting the right cushion you find a dollar!")
                    # print("Wait...it's stuck!!! Do you a) pull it off or b) use a ")
                    print("Slippers added to your cart!\n")
                    couch_money = 1
                    cash + 1

                else:
                    print("That isn't a valid option!\n")

        else:
                exit()

cash_aquisition()

#         elif choice == 'b' and 'newspaper' not in grocery_list:
#
#             newspaper_choice = 0
#
#             while newspaper_choice == 0:
#                 print("You walk down the sundries isle and can see ol' lady buscuit Barbarra eying off the last edition of 'The Daily Bake'.")
#                 print("There is no way you are going to lose to this honeybun.")
#                 dive = input("Will you dive for the paper (y/n)?\n" + prompt)
#
#                 if dive == 'y' or 'Y':
#                     print("You have won, Barbarra is down for the count and you have your newspaper\n")
#                     grocery_list.append('newspaper')
#                     grocery_list.sort()
#
#                 elif dive == 'n' or 'N':
#                     print("Through some arcane socery you have aquired the paper...Barbarra sensed your intention..."
#                           "and backflipped over horseshit to wrangle it from your claws and fell in dramaic fashion, "
#                           "leaving you the clear victor. You have your newspaper.\n")
#                     newspaper_choice = 1
#                     grocery_list.append('newspaper')
#                     grocery_list.sort()
#
#                 else:
#                     print("That isn't a valid option!\n")
#
#
#         elif choice == 'c'and 'milk' not in grocery_list:
#
#             moo_juice = 0
#
#             while moo_juice == 0:
#                 print("What milk did Mrs CCB want again...?")
#                 milk_choice = input("Was is a) full cream b) skim c) apple juice\n" + prompt)
#
#                 if milk_choice == 'a':
#                     print("Full cream...that doesn't sound right.")
#                     print("She's on the all carb no fat diet right now...\n")
#
#                 elif milk_choice == 'b':
#                     print("Yes, that's right! Enough calcium to keep her sheen, no fat to keep the appeal to the punters alive.\n")
#                     moo_juice = 1
#                     grocery_list.append('milk')
#                     grocery_list.sort()
#
#                 elif milk_choice == 'c':
#                     print("Wait a second, she was after moo-juie, not apple juice!!\n")
#
#                 else:
#                     print("That isn't a valid option!\n")
#
#
#
# shopping()
# print("You have everything required to appease Mrs CCB and perhaps learn an insight or two into what she has been doing...\n")