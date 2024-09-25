import random

class Card:
    """Class representing a single playing card."""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Class representing a deck of playing cards."""
    
    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        """Populates the deck with cards."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self._cards = [Card(rank, suit) for suit in suits for rank in ranks]

    @property
    def cards(self):
        """Returns the cards in the deck."""
        return self._cards

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self._cards)

    def deal(self, num_cards):
        """Deals a specified number of cards from the deck."""
        if num_cards > len(self._cards):
            raise ValueError("Not enough cards in the deck to deal.")
        dealt_cards = self._cards[:num_cards]
        self._cards = self._cards[num_cards:]
        return dealt_cards

class Player:
    """Class representing a player in the game."""
    
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        """Adds cards to the player's hand."""
        self.hand.extend(cards)

    def show_hand(self):
        """Displays the player's hand."""
        return f"{self.name}'s hand: {', '.join(map(str, self.hand))}"

class Game:
    """Class to manage the game."""
    
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.deck.shuffle()

    def deal_cards(self, num_cards):
        """Deals cards to each player."""
        for player in self.players:
            cards = self.deck.deal(num_cards)
            player.receive_cards(cards)

    def show_players_hands(self):
        """Displays all players' hands."""
        for player in self.players:
            print(player.show_hand())

# Example usage
if __name__ == "__main__":
    player_names = ["Alice", "Bob", "Charlie"]
    game = Game(player_names)
    game.deal_cards(5)
    game.show_players_hands()
