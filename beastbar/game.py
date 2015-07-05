"""
> game = Game()
> kristian = game.add_player("Kristian")
> lena = game.add_player("Lena")
> game.start()
Kristian play a card!
Your current deck:
1 - skunk
8 - giraffe
5 - chameleon
4 - monkey
> kristian.play_card("skunk")
Lena play a card!
...
Which animal should chameleon imitate?
...
How many animals should kangaroo skip over (1 or 2)?
...
Which species should parrot expel?
...
Game over!!!
Kristian: 5 animals in the bar (10 points) 
Lena: 4 animals in the bar (15 points)
The winner is Kristian! Congratulations!
"""

class Game:

    def __init__(self):
        self.players = []
        self.queue = JostlingArea()
        self.bar = BeastyBar()
        self.loosers = ThatsIt()

    def start(self):
        pass

    def end(self):
        pass

    def add_player(self):
        return Player()

    def get_result(self):
        pass

    def play():
        """
        How to handle events?
        We don't know yet - keep it flexible.
        Options: 
        - web interface,
        - text interface [hottest candidate for now],
          (event olver in the front end)
        - GUI
        - API
        """
        for player in players:
            self.play_card()  # ?
            self.resolve()
 


class Player:

    def __init__(self):
        self.deck = Deck.get_deck()

    def play_card(self):
        pass


class Deck(list):

    def __init__(self):
        self._build_base_deck()
        self.shuffle()

    def _build_base_deck(self):
        pass

    def shuffle(self):
       pass

    def get_hand(self):
        return self[-4:]

    def play_card(self):
        pass

class JostlingArea:
    pass


class BeastyBar:
    pass


class ThatsIt:
    pass


class MoveSolver:
    pass


class TurnSolver:
    pasS
