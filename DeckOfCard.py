class Card:
    def __init__(self, rank,suit):
        self.rank=rank
        self.suit=suit

    def get_rank(self):
        return self.rank

    def self_suit(self):
        return self.suit

    def __repr__(self):
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(card1,card2):
        return card1.rank==card2.rank


class Deck:
    def __init__(self):
        self.deck=[]
        
