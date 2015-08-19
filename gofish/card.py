class Card(object):
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] # text
    # suit = ['\uU2665, 'u2666', '/u2663', '/u2660'] # unicode symbols?
    # suits = ['-8o' '<>' '<3' '-[}' ] # ascii art?
    values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + '_' + self.suit

    def __repr__(self):
        return self.value + '_' + self.suit

    @staticmethod
    def get_all_cards():
        # initial empty deck
        cards=[]

        for s in Card.suits:
            for v in Card.values:
                cards.append(Card(suit=s,value=v))

        # one line list comprehension?
        # cards = [Card(suit=x, value=y) for x in suits for y in values]
        return cards
    
    @staticmethod
    def compare(card1, card2):
        suit1=Card.suits.index(card1.suit)
        suit2=Card.suits.index(card2.suit)
        value1=Card.values.index(card1.value)
        value2=Card.values.index(card2.value)

        # if (suits.index(card1.suit) > suits.index(card2.suit)
        if (value1 < value2 or (value1==value2 and suit1<suit2)):
            return -1
        elif (value1 > value2 or (value1==value2 and suit1>suit2)):
            return 1
        else:
            return 0 

def main():
    # testing in card functions..

    ace_of_spades=Card(suit='Spades', value='1')
    ace_of_clubs=Card(suit='Clubs', value='1')
    queen_of_hearts=Card(suit='Hearts', value='Q')
    king_of_diamonds=Card(suit='Diamonds', value='K')
    jack_of_clubs=Card(suit='Clubs', value='J')    

    # ace_of_spades=Card(suit='-[}', value='1')
    # ace_of_clubs=Card(suit='-8o', value='1')
    # queen_of_hearts=Card(suit='<3', value='Q')
    # king_of_diamonds=Card(suit='<>', value='K')
    # jack_of_clubs=Card(suit='-[}', value='J')    


    hand=[ace_of_spades,ace_of_clubs, queen_of_hearts,
          king_of_diamonds, jack_of_clubs]

    print(ace_of_spades)
    print(hand)
    
    print(ace_of_spades, ':', ace_of_clubs)
    print(Card.compare(ace_of_spades, ace_of_clubs))

    print(ace_of_spades, ':', jack_of_clubs)
    print(Card.compare(ace_of_spades, jack_of_clubs))

    print(king_of_diamonds, ':', queen_of_hearts)
    print(Card.compare(king_of_diamonds, queen_of_hearts))

#    hand.sort()
#    print(hand)

    print (Card.get_all_cards())

if __name__ == "__main__":
    main()
