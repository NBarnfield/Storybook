import random


def linebreak_adjective():
    adjective = ['incredible', 'salacious', 'enticing', 'thrilling', 'unbelievable', '']
    return random.choice(adjective)


def linebreak():
    input("\nFor more of this {} story, press any key!\n".format(linebreak_adjective()))


def goldroom():
    pass

def nexus_marketplace():
    pass


def to_be_continued():
    response = input("\nWill you take on this huge burden and get Mrs CCB her groceries (y/n)? ")
    if response == 'y':
        print("\nThe adventure is to be continued....")
        exit()

    else:
        print("\nWell the rest wasn't written yet, but I won't bother letting you know when it is written then...")
        print("Fin.")
        exit()


print("You observe an austere baked good standing by the fireplace.")
print("Upon closer inspction you notice the fierce disapproval of a woman who suffers no fools.")
print("Standing before you could be no one other than....")
print("Mrs Cream Cheese Bagel!!!")

linebreak()

print("For a moment she says nothing, yet you feel a force more engaging than gravity compel you to offer your services to this decaying elderly foodstuff.")
print('\'I need a fit strong spud like you to get my groceries for me.')
print("Mr Cranky Crumpet is just too dang cranky and I don't have time for it, Marie.")
print("I'm a busy lady with a short shelf life left.' she added as the door closed behind her")
print("A shopping list of exotic items falls flatly to the floor without pomp nor circumstance.")

linebreak()

# Setting up an empty list for the user to add items to, and a complete list that they need to aquire we can set
grocery_list = []
grocery_items = ['slippers', 'newspaper', 'milk']

def shopping():
    while grocery_list != grocery_items:
        print("You are standing in the supermaket - What would you like to find?" )
        choice = input(" a) slippers b) newspaper c) milk")

        if choice == 'a' and grocery_list != 'slippers':
            print("You walk down the sundries isle and can see ol' lady buscuit Barbarra eying off the last edition of 'The Daily Bake.")
            print("There is no way you are going to lose to this honeybun.")
            dive = input("Will you dive for the paper (y/n)? ")
            if dive = 'y' or 'Y':
                print("You have won, Barbarra is down for the count and you have your newspaper")
            else:
                print("Through some arcane socery you have aquired the paper...Barbarra sensed your intention..."
                      "and backflipped over horseshit to wrangle it from your claw and fell in dramaic fashion, "
                      "leaving you the clear vitor. You have your newspaper.")
        elif choice == 'b' and grocery_list != 'newspaper':
            pass
        elif choice == 'c'and grocery_list != 'milk':
            pass
        else:
            print("That isn't a valid option!")
            shopping()


print("You have everything required to appease Mrs CCB and perhaps learn an insight or two into what she has been doing...")

linebreak()



