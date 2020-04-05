from random import randint

class Player(object)
    def __init__(self, table_pos):
        self.table_pos = table_pos
        self.hand = []
        self.tricks = []

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

class RandomPlayer(Player):
    def __init__(self, table_pos):
        Player.__init__(self, table_pos)

    def giveCard(self, suit, preceeding_cards):
        if suit == "":
            n = randint(0,len(self.hand)-1)
            chosen_card = self.hand[n]
        else:
            cards_in_suit = []
            for card in self.hand:
                if card.suit == suit:
                    cards_in_suit.append(card)
            if len(cards_in_suit) == 0:
                n = randint(0,len(self.hand)-1)
                chosen_card = self.hand[n]
            else:
                n = randint(0,len(cards_in_suit)-1)
                chosen_card = cards_in_suit[n]
        self.hand.remove(chosen_card)
        return chosen_card

class DuckAndDump(Player):
    def __init__(self, table_pos):
        Player.__init__(self, table_pos)

    def giveCard(self, suit, preceeding_cards):
        if suit == "":
            n = randint(0,len(self.hand)-1)
            chosen_card = self.hand[n]
        else:
            cards_in_suit = []
            for card in self.hand:
                if card.suit == suit:
                    cards_in_suit.append(card)
            if len(cards_in_suit) == 0:
                n = randint(0,len(self.hand)-1)
                chosen_card = self.hand[n]
            else:
                n = randint(0,len(cards_in_suit)-1)
                chosen_card = cards_in_suit[n]
        self.hand.remove(chosen_card)
        return chosen_card
