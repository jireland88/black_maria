from random import randint
from random import shuffle

class Card(object):
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def display_card(self):
        return self.suit + str(self.value)

class Table(object):
    def __init__(self, players):
        self.players = players
        self.num_players = len(players)
        self.num_cards_per_round = int(52/self.num_players)

        self.deck = self.create_fresh_deck()

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

    def play_trick(self, inital_player_pos):
        for player in self.players:
            print("Player " + str(player.table_pos) + " has hand: " + str(player.display_hand()))

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

    def play_round(self, suit, trick_starter):
        print("Trumps: " + suit)

        self.deck = self.create_fresh_deck()
        self.deal_round(suit)

        for i in range(0, self.num_cards_per_round):
            trick_starter = self.play_trick(trick_starter)

    def play_match(self):
        print("-----NEW MATCH-----")
        self.play_round("C", 0)
        self.play_round("D", 1)
        self.play_round("H", 2)
        self.play_round("S", 3)
        self.play_round("N", 0)

    def get_scores(self):
        for player in self.players:
            print("Player " + str(player.table_pos) + " scored " + str(player.get_score()))

        scores = []
        for player in self.players:
            scores.append(player.get_score())

        return scores
