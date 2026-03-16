# Name: Ozcan Celik
# Course ID and Section: COP2002
# Date Created: March 5, 2026
# Program Title: Random MAC Address Generator
# Program Description: Generates a random MAC address using a while loop.

import random

def main():

    hexDigits = "0123456789ABCDEF"
    mac = ""
    pair = 0

    print("Generating random MAC address...")

    while(pair < 6):

        count = 0
        part = ""

        while(count < 2):
            part = part + random.choice(hexDigits)
            count = count + 1

        mac = mac + part

        if(pair < 5):
            mac = mac + ":"

        pair = pair + 1

    print(mac)


if(__name__=="__main__"):
    main()








