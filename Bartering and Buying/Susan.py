print("Before you stands Susan, a 4 foot tall lady drapped in immaculate purple finery.")
print("Behind her are a pair of slippers that you need to purchase for the Cranky Crumpet.")
print("Susan refuses to tell you her desired price and demands that you make her an offer.")

money = 0

while money == 0:
    try:
        money = float(input("How much money will you offer? "))
    except:
        print("That is not a monetary value!! Get it together and look in your purse, Barbarra!")
        print("Look again!!")

if  money >= 10.50:
    print("'I will take all of that thank you very much.' she proclaims as she scurries into the dark night that appeared from nowhere.")
    print("You have the slippers!! And have paid well over market value for secondhand footwear.")
elif money >= 6.50:
    print("She sizes you up and finally declares - 'Give me what you've got and a coffee card and we're even...'")
    print("Success, the slippers are yours!!! Shame you'll be a barista forever.")
else:
    print("Clearly abhorred with the pitence offered she cried 'Don't even worry about it, kid. You've got your own problems clearly....'")
    print("You danced with the devil and won. Good for you, Porkchop!")