from random import randint
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt

class Card(object):
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def display_card(self):
        return self.suit + str(self.value)

class Player(object):
    def __init__(self, table_pos):
        self.table_pos = table_pos
        self.hand = []
        self.tricks = []

    def giveCard(self, suit, preceeding_cards):
        if suit == "":
            n = randint(0,len(self.hand)-1)
            chosen_card = self.hand[n]

        cards_in_suit = []
        for card in self.hand:
            if card.suit == suit:
                cards_in_suit.append(card)
        if len(cards_in_suit) == 0:
            n = randint(0,len(self.hand)-1)
            chosen_card = self.hand[n]
            self.hand.remove(chosen_card)
            return chosen_card
        else:
            n = randint(0,len(cards_in_suit)-1)
            chosen_card = cards_in_suit[n]
            self.hand.remove(chosen_card)
            return chosen_card

    def get_score(self):
        score = 0
        for trick in self.tricks:
            for card in trick:
                score += card.score
        return score

    def display_hand(self):
        to_return = ""
        for card in self.hand:
            to_return += card.display_card()
        return to_return



class Table(object):
    def __init__(self, num_players):
        self.players = []
        self.num_players = num_players
        self.num_cards_per_round = int(52/num_players)

        self.deck = self.create_fresh_deck()

        for i in range(0, self.num_players):
            self.players.append(Player(i))

    def create_fresh_deck(self):
        new_deck = []
        for i in range(2,11):
            new_deck.append(Card("C", i, 0))
            new_deck.append(Card("D", i, 0))
            new_deck.append(Card("H", i, i))
            new_deck.append(Card("S", i, 0))
        new_deck.append(Card("C", 11, 0))
        new_deck.append(Card("D", 11, 0))
        new_deck.append(Card("H", 11, 10))
        new_deck.append(Card("S", 11, 0))
        new_deck.append(Card("C", 12, 0))
        new_deck.append(Card("D", 12, 0))
        new_deck.append(Card("H", 12, 10))
        new_deck.append(Card("S", 12, 25))
        new_deck.append(Card("C", 13, 0))
        new_deck.append(Card("D", 13, 0))
        new_deck.append(Card("H", 13, 10))
        new_deck.append(Card("S", 13, 0))
        new_deck.append(Card("C", 14, 0))
        new_deck.append(Card("D", 14, 0))
        new_deck.append(Card("H", 14, 15))
        new_deck.append(Card("S", 14, 0))

        return new_deck

    def deal_round(self, suit):
        for card in self.deck:
            if card.suit == suit:
                card.value += 100

        shuffle(self.deck)

        for i in range(0, len(self.players)):
            lower_bound = int((52/self.num_players)*i)
            upper_bound = int((52/self.num_players)*(i+1))
            self.players[i].hand = self.deck[lower_bound:upper_bound]
            # display hand function

    def play_trick(self, inital_player_pos):
        trick = []
        values = []

        card = self.players[inital_player_pos].giveCard("", trick)
        print("Player " + str(inital_player_pos) + " gave card " + card.display_card())
        trick.append(card)
        values.append(card.value)
        suit = card.suit

        for i in range(1, len(self.players)):
            player_num = (inital_player_pos + i) % self.num_players
            card = self.players[player_num].giveCard(suit, trick)
            print("Player " + str(self.players[player_num].table_pos) + " gave card " + card.display_card())
            trick.append(card)
            values.append(card.value)

        winning_player = (inital_player_pos + values.index(max(values))) % self.num_players
        self.players[winning_player].tricks.append(trick)

        print("Trick won by " + str(winning_player))

        return winning_player

    def play_round(self, suit):
        print("Trumps: " + suit)

        self.deck = self.create_fresh_deck()

        self.deal_round(suit)

        trick_starter = randint(0,self.num_players-1)

        for i in range(0, self.num_cards_per_round):
            trick_starter = self.play_trick(trick_starter)

    def get_scores(self):
        for player in self.players:
            print("Player " + str(player.table_pos) + " scored " + str(player.get_score()))

        return self.players[0].get_score()



scores = []
for q in range(0,1000):
    table = Table(4)
    table.play_round("C")
    table.play_round("D")
    table.play_round("H")
    table.play_round("S")
    table.play_round("N")
    scores.append(table.get_scores())

print("mean score: " + str(np.mean(scores)))
print("std score: " + str(np.std(scores)))

plt.hist(scores, 10)
plt.show()
