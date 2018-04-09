import random

def linebreak_adjective():
    adjective = ['incredible', 'salacious', 'enticing', 'thrilling']
    return random.choice(adjective)

def linebreak():
    input("\nFor more of this {} story, press any key!\n".format(linebreak_adjective()))


linebreak()
linebreak()
linebreak()
linebreak()