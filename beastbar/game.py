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

class IllegalAction(Exception): pass

class Game:

    def __init__(self):
        self._running = False
        self._player_gen = None
        self.players = []
        self.queue = JostlingArea()
        self.bar = BeastyBar()
        self.loosers = ThatsIt()

    def start(self):
        self._running = True

    def end(self):
        self._running = False

    def is_running(self):
        return self._running

    def add_player(self, player):
        if not self._running:
            self.players.append(player)
            self._player_gen = self._generate_players()
        else:
            raise IllegalAction("Cannot add player. Game already running.")

    def _generate_players(self):
        while True:
            for p in self.players:
                if p.has_cards_left():
                    yield p

    def next_player(self):
        return next(self._player_gen)

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

    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.hand = self.deck.get_hand()

    def get_hand_names(self):
        return ['Hippo', 'Lion', 'Skunk', 'Zebra'] # !!!
        names = [animal.name for animal in self.hand]

    def play_card(self, animal):
        if not animal in self.get_hand_names():
            raise Exception("Player %s has no animal '%' in his hand." % (self.name, animal))
        animal.enter_queue()

    def has_cards_left(self):
        return True
        if len(self.hand) > 0:
            return True


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

class JostlingArea(list):

    def has_animal(self, animal_name):
        any(card.is_animal(animal_name) for card in self)
            
    def remove_animal(self, animal_name):
        x = len(self)
        while x > 0:
            if self[x-1].is_animal(animal_name):
                self.pop(x-1)
            x -= 1 


class BeastyBar:
    pass


class ThatsIt:
    pass


class MoveSolver:
    pass


class TurnSolver:
    pass
