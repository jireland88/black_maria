from blackmaria import Card
from random import randint


class Player(object):
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
            # display hand function
class DuckAndDumpAgressive(Player):
    def __init__(self, table_pos):
        Player.__init__(self, table_pos)

    def giveCard(self, suit, preceeding_cards):
        chosen_card = Card("NULL", -1, -1)
        if suit == "":
            # choose lowest card of any suit
            print("Ducking and leading")
            values = []
            for card in self.hand:
                if card.suit == suit:
                    values.append(card.value - 100)
                else:
                    values.append(card.value)

            n = values.index(min(values))

            chosen_card = self.hand[n]

        else:
            cards_in_suit = []
            for card in self.hand:
                if card.suit == suit:
                    cards_in_suit.append(card)
            if len(cards_in_suit) == 0:
                # dump queen of spades or highest heart
                print("Dumping")
                points = []
                for card in self.hand:
                    points.append(card.score)
                n = points.index(max(points))
                chosen_card = self.hand[n]
            else:
                # play highest card under leading, or lowest card

                # get leading card
                trick_values = []
                for card in preceeding_cards:
                    trick_values.append(card.value)
                leading_card = preceeding_cards[trick_values.index(max(trick_values))]

                cards_that_duck = []
                for card in cards_in_suit:
                    if card.value < leading_card.value:
                        cards_that_duck.append(card)

                if len(cards_that_duck) > 0:
                    print("Ducking safely")
                    duck_values = []
                    for card in cards_that_duck:
                        duck_values.append(card.value)
                    chosen_card = cards_that_duck[duck_values.index(max(duck_values))]
                else:
                    print("Ducking dangerously")
                    valid_values = []
                    for card in cards_in_suit:
                        valid_values.append(card.value)
                    chosen_card = cards_in_suit[valid_values.index(min(valid_values))]
                    
        self.hand.remove(chosen_card)
        return chosen_card
