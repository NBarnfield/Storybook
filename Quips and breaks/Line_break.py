import random


def linebreak():
    adjective = ['incredible', 'salacious', 'enticing', 'thrilling']
    input("\nFor more of this {} story, press any key!\n".format(random.choice(adjective)))

def user_name():
    while True:
        name = input("Hello friend! What is your name?")
        #TODO: Make sure str validation works ---- if isinstance(name, str):
            if len(name) < 4:
                print("{}...That is a short name! You must hear that a lot...".format(name))
                return name
            else:
                print("Welcome {}!".format(name))
                return name
        else:
            print("That's not a name! We're not living in flatland you know. Try again, and no fibbing this time.")


name = user_name()
linebreak()
print(name)
linebreak()
print(name)
linebreak()
print(name)
linebreak()