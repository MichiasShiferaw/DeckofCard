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
    suits={'\u2660','\u2663','\u2665','\u2666'}
    ranks={"2","3","4","5","6","7","8","9","10","J","Q","K","A"}
    def __init__(self):
        self.deck=[]
        for rank in Deck.ranks:
            for suit in Deck.suits:
                self.deck.append( Card(rank,suit) )
    def shuffle(self):
        random.shuffle(self.deck)
	#d1.deck
        #d1.shuffle()
