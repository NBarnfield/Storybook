import random


def random_adjective():
    adjectives = ['incredible', 'salacious', 'enticing', 'thrilling', 'ambitious', 'witty', 'frolicsome', 'dazzling', 'resplendent', 'vivid']

    return random.choice(adjectives)


def linebreak():
    input("\nFor more of this {} story, press any key!\n".format(random_adjective()))


linebreak()
linebreak()
linebreak()
linebreak()