from random import shuffle
from card import Card

class Deck(object):

    # suit and values are determined from the standard french 52 card deck
    
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__ (self):
        self.deck = Card.get_all_cards()
        shuffle(self.deck)
       
    def draw_card(self):
        return self.deck.pop()

    def cards_remaining(self):
        return len(self.deck)

    def __repr__(self):
        return '{num} cards remaining in the deck.'.format(num=self.cards_remaining)

    def __str__(self):
        return '{num} cards remaining in the deck.'.format(num=self.cards_remaining)

# main function to test shuffle and draw functions
def main():
    deck = Deck()

    # print and iterate over the whole deck
    while deck.cards_remaining() > 0:
        #print(deck)
        card = deck.draw_card()
        print(deck.cards_remaining(), ':', card)


if __name__ == "__main__":
    main()
