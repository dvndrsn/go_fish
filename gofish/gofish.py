from deck import Deck
from card import Card
from player import Player
import os
import sys

class GoFish(object):

    # initialize deck andd players
    def __init__(self, num_human_players, num_computer_players, debug=False):
        self.deck = Deck()
        self.num_players = num_human_players # + num_computer_players
        self.players = []
        self.debug=debug

        # determine hand size and exit if players count is not acceptable
        if self.num_players > 8 or self.num_players == 1:
            sys.exit()
        elif self.num_players > 4:
            starting_hand_size = 5
        else:
            starting_hand_size = 7
        
        # add the human players
        for p in range(num_human_players):
            self.players.append(Player()) # HumanPlayer

        # add the computer players
        # for c in range(num_computer_players):
        #     self.players.append(ComputerPlayer())

        # deal initial set of cards for each player
        for c in range(starting_hand_size):
            for p in range(self.num_players):
                self.players[p].take_cards(self.deck.draw_card())

        # default game values
        self.num_turns = 1
        self.current_player=1

        # start it up! 
        self.play_go_fish()

    def play_go_fish(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        while self.deck.cards_remaining()>0:
            ### START TURN ###
            print("*** Go Fish!!! ***\n*** Turn # {t} ***\n".format(t=self.num_turns))

            # show the sets for all players
            for p in range(1,self.num_players+1):
                print("Player {p} has {s} sets:".format(p=p,
                    s=len(self.players[p-1].sets)))
                self.players[p-1].show_sets()

            # display the current player's hand
            print("Player {p}'s turn.\n".format(p=self.current_player))
            self.players[self.current_player-1].show_hand() 

            ### GET INPUT ###
            # ask the current player who should be the fishing target
            # target_player = self.get_target_player()
            target_player = self.players[self.current_player].get_target_player(
                self.current_player, self.players)

            ############ for debug, cheat a little :) ##########
            if self.debug==True:
                print("DEBUG: Shh.. Here's the other player's hand(!!!):")
                print(self.players[target_player-1].hand)

            # take a guess to fish for from the current player
            # guess_value = self.get_guess_value()
            guess_value = self.players[self.current_player].get_guess_value(Card.values,
                self.players)

            ### GO FISH ###
            print("\nPlayer {p} is fishing for any cards with value {v}".format(
                p=self.current_player, v=guess_value) + " from Player {t}.".format(
                t=target_player))
            
            # take those cards from the target player or go fish
            fished_cards = self.players[target_player-1].give_cards(guess_value)

            if len(fished_cards)==0:
                print("Go fish!!!")
                fished_card=self.deck.draw_card()
                print("Player {p} picked up the card: {c}\n".format(p=self.current_player,
                    c=fished_card))
                self.players[self.current_player-1].take_cards(fished_card)
            else:
                print("Player {p} fished {nc} card(s) from ".format(p=self.current_player,
                    nc=len(fished_cards)) + "Player {tp}!\n".format(tp=target_player))
                self.players[self.current_player-1].take_cards(*fished_cards)

            ### END TURN ##
            # play sets and end turn
            played_set_count = self.players[self.current_player-1].play_sets()
            print("Player {p} played {s} new sets.\n".format(p=self.current_player,
                s=played_set_count))

            # change turns if the current player didn't fish any cards from another player
            if len(fished_cards)==0 and fished_card.value!=guess_value:
                self.current_player = target_player
            else:
                print("Lucky! You fished successfully and will go again!\n")

            input("Ready for the next turn? Player {p} is up. ".format(
                p=self.current_player) + "Everyone else: avert your eyes! " +
                "Hit enter to proceed.")

            # start with a fresh screen for our next turn
            os.system('cls' if os.name == 'nt' else 'clear')
            self.num_turns+=1

        ### FINISH GAME ###
        print ("After {nt} turns there are no more fish ".format(nt=self.num_turns) +
            "in the pond. This is an ecological disaster! Time to check for the winner!")

        check_winner()


    def get_target_player(self):
        # show player list 
        print("\nWho would you like to take cards from?")
        for p in range(1,self.num_players+1):
            if p != self.current_player:
                print("    x. Player {num}: {c} cards".format(num=p, c=len(self.players[p-1].hand)))

        # get input 
        target_player = 0
        while (target_player <= 0 or target_player > self.num_players
                or target_player == self.current_player):
            target_player = input('\nEnter player number: ')
            try:    
                target_player=int(target_player)
            except ValueError:
                target_player=0
        return target_player

    def get_guess_value(self):
        print ("\nCards in the deck: ", Card.values)

        guess_value = ''
        while (Card.values.count(guess_value)==0):
             guess_value = input('\nWhat card would you like to guess? ')
        return guess_value

    def check_winner(self):
        highest_set_count = 0
        winning_player = 0

        for p in range(self.num_players):
            set_count = len(self.players(p).sets)
            if set_count > highest_set_count:
                highest_set_count = set_count
                winning_player = p+1
        
        print("Player {p} won with {s} sets after {t} turns!".format(p=winning_player),
            s=highest_set_count, t=self.num_turns)
        
def main():
    debug = input("Start debug mode (y/n)? ") in ['Y','y']
    num_human_players = int(input("Number of human players? "))
    num_computer_players = int(input("Number of computers players? "))

    go_fish = GoFish(num_human_players, num_computer_players, debug)

if __name__ == '__main__':
    main()