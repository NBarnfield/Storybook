import random


def linebreak_adjective():
    adjective = ['incredible', 'salacious', 'enticing', 'thrilling']
    return random.choice(adjective)


def linebreak():
    input("\nFor more of this {} story, press any key!\n".format(linebreak_adjective()))


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

response = input("Will you take on this huge burden and get Mrs CCB her groceries (y/n)? ")
if response == 'y':
    print("\nThe adventure is too be continued....")

else:
    print("\nWell the rest wasn't written yet, but I won't bother letting you know when it is written then...")
    print("Fin.")
