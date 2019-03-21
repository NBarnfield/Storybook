def block_text(source_file):
    file_for_parsing = open(source_file, "r")
    for line in file_for_parsing:
        input(line)


def leave_story():
    exit_story = input("\n..................................................."
                       "Press any key to continue, or type exit to leave..."
                       "...................................................\n")
    if exit_story.lower() == "exit":
        quit()


def beginning_text():
    input("We are about to embark on an incredible tale epic in size, coming to you straight from the Giggle Galaxy! "
          "Press any key to continue...\n")

def prompt():
    input(">>> ")

# def utility(risk_aversion):
#     'Adaptation of the quadratic utility function to determine if a good is an acceptable price in the game'
#     user_utility =
