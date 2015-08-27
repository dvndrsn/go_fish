from card import Card
from random import shuffle

class Player(object):
    def __init__(self):
        self.hand=[]
        self.sets=[]

    def play_sets(self):
        set_count = 0
        for c in self.hand:
            card_count=0
            for p in self.hand:
                if (c.value==p.value): # TODO bug here (function has no such attrubute 'value'?)
                    card_count+=1
            # count values (set assumes four of a kind)
            if card_count==4:
                self.sets.append(self.give_cards(c.value))
                set_count+=1
        return set_count

    def count_sets(self):
        set_count=0

    # need to use * when calling with a long list of cards..
    def take_cards(self, card, *cards):
        self.hand.append(card)

        self.hand.extend(cards)

    def give_cards(self, value):
        fished_cards = []
        num_searched=0

        # print("Searching for {v}.".format(v=value))
        # print("Hand size is {h}.".format(h=len(self.hand)))

        # iterate over a copy of the list so entries can be removed as we go
        for c in self.hand[:]:
            num_searched+=1
            if c.value == value:
                fished_cards.append(c)
                self.hand.remove(c)
        
        # remove items afterwards (was causing a bug while removing during)
        # TODO - research removing items from list while iterating
        # need to use list comprehnsions
        # for c in fished_cards:
            

        # print("Searched {s} cards.".format(s=num_searched))
        # print("Fished size is {h}.".format(h=len(fished_cards)))
        # print("Hand size is {h}.".format(h=len(self.hand)))

        return fished_cards

    def show_sets(self):
        print(self.sets)
        print()

    def show_hand(self):
        print("Here's your hand:")
        for card in self.hand:
            print("    {c}".format(c=card))
        print()

    # pass as abstract
    def get_target_player(self, current_player, players):
        print("\nWho would you like to take cards from?")

        num_players = len(players)

        for p in range(1,num_players+1):
            if p != current_player:
                print("    x. Player {num}: {c} cards".format(num=p, c=len(players[p-1].hand)))

        # get input 
        target_player = 0

        while (target_player <= 0 or target_player > num_players
                or target_player == current_player):
            target_player = input('\nEnter player number: ')
            try:
                target_player=int(target_player)
            except ValueError:
                target_player=0
        return target_player

    # pass as abstract
    def get_guess_value(self, values, players):
        print ("\nCards in the deck: ", values)

        guess_value = ''

        while (values.count(guess_value)==0):
             guess_value = input('\nWhat card would you like to guess? ')
        return guess_value

def main():
    player=Player()
    player2=Player()

    # player.take_cards(Card('Hearts','Q'), Card('Spades','J'))
    all_cards=Card.get_all_cards()
    shuffle(all_cards)
    player.take_cards(*all_cards)

    print("Player1:")
    player.show_hand()
    print("Player2:")
    player2.show_hand()

    player2.take_cards(*player.give_cards('5'))

    print("Player1:")
    player.show_hand()
    print("Player2:")
    player2.show_hand()

    kings=player.give_cards('K')
    jacks=player.give_cards('J')
    queens=player.give_cards('Q')
    aces=player.give_cards('1')

    print("Took {c} Kings from P1.".format(c=len(kings)))
    print("Took {c} Jacks from P1.".format(c=len(jacks)))
    print("Took {c} Queens from P1.".format(c=len(queens)))
    print("Took {c} Acess from P1.".format(c=len(aces)))

    player2.take_cards(*kings)
    player2.take_cards(*jacks)
    player2.take_cards(*queens)
    player2.take_cards(*aces)


    print("Player1's hand:")
    player.show_hand()
    print("Player2's hand:")
    player2.show_hand()

    players = [player,player2]

    target=player.get_target_player(1, players)
    print("Chose target player: {p}".format(p=target))

    target=player.get_guess_value(Card.values, players)
    print("Chose guess value: {v}".format(v=target))

    # sets = player.play_sets()
    # print("Player1's hand:")
    # player.show_hand()
    # print ("Player 1 has this many sets:" + str(sets) )
    # print (player.sets)
    
    # sets2=player2.play_sets()
    # print("Player2's hand:")
    # player2.show_hand()
    # print ("Player 2 has this many sets sets:" + str(sets2) )
    # print (player2.sets)

if __name__ == '__main__':
    main()