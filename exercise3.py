# Ozcan Celik
# W26 COP2002-0T1
# February 5, 2026
# Exercise 3 - UNO Card Color Identifier
# Program randomly selects an UNO card and determines its color or identifies it as a wild card.

def main():
    # **************DO NOT MODIFY ANYTHING BELOW THIS LINE***************************
    from random import randint

    # Contains a representation of each of the cards used in Uno's basic card deck.
    # An image file would need to be associated with each value to be able to show the card
    # to the user.
    unoCardDeck=['BLUE_1', 'BLUE_1', 'BLUE_2', 'BLUE_2', 'BLUE_3', 'BLUE_3', 'BLUE_4', 
                'BLUE_4', 'BLUE_5', 'BLUE_5', 'BLUE_6', 'BLUE_6', 'BLUE_7', 'BLUE_7', 
                'BLUE_8', 'BLUE_8', 'BLUE_9', 'BLUE_9', 'BLUE_0', 'BLUE_SKIP', 
                'BLUE_SKIP', 'BLUE_+2', 'BLUE_+2', 'BLUE_REVERSE', 'BLUE_REVERSE', 
                'GREEN_1', 'GREEN_1', 'GREEN_2', 'GREEN_2', 'GREEN_3', 'GREEN_3', 
                'GREEN_4', 'GREEN_4', 'GREEN_5', 'GREEN_5', 'GREEN_6', 'GREEN_6', 
                'GREEN_7', 'GREEN_7', 'GREEN_8', 'GREEN_8', 'GREEN_9', 'GREEN_9', 
                'GREEN_0', 'GREEN_SKIP', 'GREEN_SKIP', 'GREEN_+2', 'GREEN_+2', 
                'GREEN_REVERSE', 'GREEN_REVERSE', 
                'YELLOW_1', 'YELLOW_1', 'YELLOW_2', 'YELLOW_2', 'YELLOW_3', 'YELLOW_3', 
                'YELLOW_4', 'YELLOW_4', 'YELLOW_5', 'YELLOW_5', 'YELLOW_6', 'YELLOW_6', 
                'YELLOW_7', 'YELLOW_7', 'YELLOW_8', 'YELLOW_8', 'YELLOW_9', 'YELLOW_9', 
                'YELLOW_0', 'YELLOW_SKIP', 'YELLOW_SKIP', 'YELLOW_+2', 'YELLOW_+2', 
                'YELLOW_REVERSE', 'YELLOW_REVERSE', 
                'RED_1', 'RED_1', 'RED_2', 'RED_2', 'RED_3', 'RED_3', 'RED_4', 'RED_4', 
                'RED_5', 'RED_5', 'RED_6', 'RED_6', 'RED_7', 'RED_7', 'RED_8', 'RED_8', 
                'RED_9', 'RED_9', 'RED_0', 'RED_SKIP', 'RED_SKIP', 'RED_+2', 'RED_+2', 
                'RED_REVERSE', 'RED_REVERSE', 
                '+4', '+4', '+4', '+4', 
                'WILD', 'WILD', 'WILD', 'WILD']

    # Pick a random card's index
    randomCardIndex=randint(0,len(unoCardDeck)-1)  

    # Print random index chosen
    print(f"Index chosen is {randomCardIndex}.")

    # Determine the random card
    randomCard=unoCardDeck[randomCardIndex]

    # The prevous two lines of code could be combined to have one more complex line of code 
    # randomCard=unoCardDeck[randint(0,len(unoCardDeck)-1)] # equivalent to the previous 2 lines of code

    # Print what the randomCard is
    print(f"The random card is {randomCard}.")

    # **************DO NOT MODIFY ANYTHING ABOVE THIS LINE***************************


    # Determine what color the card is or if the card is a special card.
    if randomCard == "WILD" or randomCard == "+4":
        print("This card is a type of wild card (either wild or draw four).")
    else:
        color = randomCard.split("_")[0]
        print(f"The color of the card is {color}.")


    # TODO: Write your if / elif / else here
    # Requirements reminder:
    # - If randomCard is "WILD" or "+4" -> print the exact wild sentence from the rubric
    # - Else -> print: "The color of the card is COLOR."
    #   where COLOR is ONLY the color word (BLUE/RED/YELLOW/GREEN), not "BLUE_7"

if __name__ == "__main__":
    main()

