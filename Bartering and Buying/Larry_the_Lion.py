import storybook

storybook.block_text("Larry_the_lion_beginning.txt")
storybook.leave_story()
storybook.block_text("Larry_the_lion_description_1.txt")

yoga_ball = 0

while yoga_ball == 0:
    try:
        money = float(input("'10.50 is the going rate...' he growls.\n How much money will you offer?\n"))
        if money >= 10.50:
            print("I see you aren't one for making a game of money. Frankly, what you've offered would be robbery on my part if I took it. I'm not above robbery.\n")
            print("Larry throws you the ball and vanishes with the assistance of an unnecessary smoke bomb.\n")
            print("You have the yoga ball!! And have paid well over market value for secondhand sports equipment.\n")
            yoga_ball = 1
        elif money >= 6.50:
            print("Feigning dissatisfaction and resentment, Larry nods his head apparently weighing up your offer.\n"
                  "'You drive a hard bargain.' he claims, knowing full well that you are purchasing junk.\n")
            print("Larry throws you the ball and vanishes with the assistance of an unnecessary smoke bomb.\n")
            print("You have the yoga ball!! And have paid well over market value for secondhand sports equipment.\n")
            yoga_ball = 1
        else:
            print("Larry falls to the ground, seemingly shocked and appaled by the pitence you have offered. The thespian takes delight in exclaiming...\n")
            print("'Nonesense, this is a top of the line yoga ball straight from the FUTURE. That's right, it's instore before they've even designed it.'\n")
            print("It seems you will have to offer more if you want to get the yoga ball and get Kranky Krumpet off your case...\n")
    except ValueError:
        print("That is not a monetary value!! Get it together and look in your purse, Barbarra!\n")
        print("Look again!!\n")


print("Upon returning home, you find Kranky Krumpet stretched out in front of the fire with a yoga ball that he had stored in the attic.\n"
      "You go to the viewing deck and stare into nothingness wondering what you could have done with you day.\n"
      "At least you still have soy candles you didn't realise you'd purchased.")
