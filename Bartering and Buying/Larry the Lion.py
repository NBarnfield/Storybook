print("You approach a cave with tender foot. Carefully breathing shallow breaths. In, and out.")
print("Larry the Lion approaches with eyes ablaze. You tread here knowing that he has had a bad sleep...")
print("You need to get Kranky Krumpet a yoga ball so he can stretch out his gluten.")
print("Larry the LIon is the store person who stocks them")

lion_treats = 3

while lion_treats >= 1:
    try:
        #TODO: Write up that Larry needs treats to calm him down. ONce he has the treats he is fine to talk and give you the yoga ball print("You have ")
        happiness_factor = float(input("How much money will you offer? "))
        if happiness_factor >= 10.50:
            print("")
            print("")
            print("")
        elif happiness_factor >= 6.50:
            print("")
            print("")
        else:
            print("")
            print("")
            print("")
    except ValueError:
        print("")
        print("")

print("I feel so much better!!! Says Larry.")
print("Of course you can have a yoga ball!! We don't want Krank Krumpet getting crusty!")

yoga_ball = 1
