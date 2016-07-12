import random

def genSeed():
    x = None
    chars = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    seed = ""
    while (len(seed) < 81):
        seed += chars[random.randint(0, len(chars) - 1)]

    print ("Generated random seed!\n")
    return seed

print (genSeed())
