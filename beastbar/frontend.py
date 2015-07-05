#!/usr/bin/python3

from game import Game

ANIMALS = {
    "1": "Skunks",
    "2": "Parrot",
    }

class TextFrontend:

    def __init__(self):
        self.game = None

    def enter_animal():
        for num in ANIMALS:
            print("%s\t%s" % (num, ANIMALS[num]))
        print("x\tEXIT")
        print("")
        choice = input("")
        animal = ANIMALS.get(choice, 'x')
        return animal

    def print_queue(self):
        print("\nQueue status: []\n")

    def create_game():
        self.game = Game()
        self.game.add_player(Player("Kristian"))
        self.game.add_player(Player("Lena"))
        self.game.start()

    def run_game(game):
        while not self.game.ended:
            animal = "-"
            for p in game.players:
                self.print_queue()
                animal = self.enter_animal(player)
                if animal != 'x':
                    print ("a %s enters the queue." % animal)
                    player.play_card(animal)

    def finalize_game(game):
        result = self.game.get_result()
        self.print_result(result)
        self.game.end()
        self.game = None

